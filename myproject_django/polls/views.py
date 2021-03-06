import pandas as pd
from .models import *
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse

@csrf_exempt
def upload(request):
    question_excel_file = request.FILES.get("question_excel_file",False)
    if question_excel_file:
        question_df=pd.read_excel(question_excel_file,sheet_name=0)
        question_array=question_df.values
        question_manager=Question.objects
        classification_manager=Classification.objects
        for arr in question_array:
            question_manager.create_by_arr(arr)

    answer_excel_file=request.FILES.get("answer_excel_file",False)
    if answer_excel_file:
        answer_df=pd.read_excel(answer_excel_file,sheet_name=0)
        columns=answer_df.columns.tolist()
        for index in range(2,len(columns)):
            columns[index]=re.split('[\D]+',columns[index])
            question=question_manager.get(number=columns[index][2])
            columns[index]=question


        for index_row, row in answer_df.iterrows():
            person=Person.objects.create(name=row[0],email=row[1])
            for index in range(2,len(row)):
                row[index]=re.sub('[\W]+','',row[index])
                answer=Answer.objects.get(question=columns[index],answer=row[index])
                person.answers.add(answer)
            person.save()
    return True

def person_by_page(request,current_page,num=10):
    response={}
    persons={}
    count=len(Person.objects.all())
    for person in Person.objects.all()[(current_page-1)*num:(current_page)*num]:
        person_list=person.to_list()
        person_list[2]=[str(value) for value in person_list[2]]
        persons[person.id]={
            "name":person_list[0],
            "email":person_list[1],
            "answers":person_list[2]
            }
    response['persons']=persons
    columns=['name','email']
    for question in Question.objects.all().order_by('number'):
        columns.append(str(question.number))
    response['columns']=columns
    response['count']=count
    return JsonResponse(response)

def answer_rate_by_page(request,current_page,num=10):
    response={}
    answer_rate={}
    count=len(Question.objects.all())
    for question in Question.objects.all()[(current_page-1)*num:(current_page)*num]:
        answer_rate[question.number]={}
        for answer in question.answer_set.all():
            answer_rate[question.number][str(answer)]=0
    for person in Person.objects.all():
        for answer in person.answers.all():
            answer_rate[answer.question.number][str(answer)]=answer_rate[answer.question.number][str(answer)]+1
    response['columns']=[str(answer) for answer in Question.objects.all().first().answer_set.all()]
    response['answer_rate']=answer_rate
    response['count']=count
    return JsonResponse(response)