import pandas as pd
from polls.models import *

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

def person(request,person_id):
    if person_id == -1:
        persons=[]
        for person in Person.objects.all():
            persons.append(person.answers.objects.all())
        return persons
