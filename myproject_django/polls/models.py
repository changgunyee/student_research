from django.db import models
import re
# Create your models here.
class ClassificationManager(models.Manager):
    def create_by_arr(self,array):
        query_c=self.filter(section=array[0],type1=array[1],type2=array[2])
        #import pdb;pdb.set_trace()
        if query_c.exists():
            return query_c[0]
        else:
            c=self.create(section=array[0],type1=array[1],type2=array[2])
            return c

class Classification(models.Model):
    section=models.IntegerField()
    type1=models.CharField(max_length=20)
    type2=models.CharField(max_length=20)
    objects=ClassificationManager()
    def __str__(self):
        return str(self.section)+"->"+self.type1+"->"+self.type2

class QuestionManager(models.Manager):
    def create_by_arr(self,array):
        query_q=self.filter(number=array[0])
        if query_q.exists():
            return query_q[0]

        classification_manager=Classification.objects
        c=classification_manager.create_by_arr(array[1:4])
        q=self.create(number=array[0],classification=c,text=array[4])

        answer_type_arr=array[5].split(',')
        answer_type_arr=[re.sub('[\W]+','',str) for str in answer_type_arr]
        for answer_type in answer_type_arr:
            Answer.objects.create(question=q,answer=answer_type)
        return q

class Question(models.Model):
    number=models.IntegerField(primary_key=True)
    classification=models.ForeignKey(Classification,on_delete=models.CASCADE)
    text=models.TextField()
    objects=QuestionManager()
    def __str__(self):
        return self.text

class Answer(models.Model):
    question=models.ForeignKey(Question,on_delete=models.CASCADE)
    answer=models.CharField(max_length=20)
    def __str__(self):
        return self.answer



class Person(models.Model):
    name=models.CharField(max_length=20)
    email=models.CharField(max_length=100)
    answers=models.ManyToManyField(Answer)
    def __str__(self):
        return self.name
    def to_list(self):
        return [self.name,self.email,list(self.answers.all().order_by('question__number'))]
    class Meta:
        indexes=["name","email","answers"]

