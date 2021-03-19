from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .forms import AnswerForm
import csv
import review.analy
import review.ML_model
import time

from .models import Result


# Create your views here.


def index(request):
    form = AnswerForm(request.POST or None)
    if form.is_valid():
        print("form good")
        obj = Result()
        obj.Name = form.cleaned_data['Name']
        obj.Question1 = form.cleaned_data['Question1']
        obj.Question2 = form.cleaned_data['Question2']
        obj.Question3 = form.cleaned_data['Question3']
        obj.Question4 = form.cleaned_data['Question4']
        obj.Question5 = form.cleaned_data['Question5']
        obj.Question6 = form.cleaned_data['Question6']
        obj.Question7 = form.cleaned_data['Question7']
        obj.Question8 = form.cleaned_data['Question8']
        obj.Question9 = form.cleaned_data['Question9']
        obj.Question10 = form.cleaned_data['Question10']
        obj.Question11 = form.cleaned_data['Question11']
        obj.Question12 = form.cleaned_data['Question12']
        obj.Question13 = form.cleaned_data['Question13']
        obj.Question14 = form.cleaned_data['Question14']
        obj.Question15 = form.cleaned_data['Question15']
        obj.Question16 = form.cleaned_data['Question16']
        obj.Question17 = form.cleaned_data['Question17']
        obj.Question18 = form.cleaned_data['Question18']
        obj.Question19 = form.cleaned_data['Question19']
        obj.Question20 = form.cleaned_data['Question20']
        obj.Question21 = form.cleaned_data['Question21']
        obj.Question22 = form.cleaned_data['Question22']
        obj.Question23 = form.cleaned_data['Question23']
        obj.Question24 = form.cleaned_data['Question24']
        obj.Question25 = form.cleaned_data['Question25']
        obj.Question26 = form.cleaned_data['Question26']
        obj.Question27 = form.cleaned_data['Question27']
        obj.Question28 = form.cleaned_data['Question28']
        obj.Question29 = form.cleaned_data['Question29']
        obj.Question30 = form.cleaned_data['Question30']
        obj.Question31 = form.cleaned_data['Question31']
        obj.Question32 = form.cleaned_data['Question32']
        obj.Question33 = form.cleaned_data['Question33']
        obj.Question34 = form.cleaned_data['Question34']
        obj.Question35 = form.cleaned_data['Question35']
        obj.Question36 = form.cleaned_data['Question36']
        obj.Question37 = form.cleaned_data['Question37']
        obj.Question38 = form.cleaned_data['Question38']
        obj.Question39 = form.cleaned_data['Question39']
        obj.Question40 = form.cleaned_data['Question40']

        obj.save()

        file = str(Result.objects.values_list('Name').order_by('-pk')[0])
        file = file.replace("'", "")
        CSV_PATH1 = 'before_analy' + file + '.csv'
        with open(CSV_PATH1, 'w', encoding='utf-8', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            writer.writerow(
                ['Name', 'Question1', 'Question2', 'Question3', 'Question4', 'Question5', 'Question6', 'Question7',
                 'Question8', 'Question9', 'Question10',
                 'Question11', 'Question12', 'Question13', 'Question14', 'Question15', 'Question16', 'Question17',
                 'Question18', 'Question19', 'Question20',
                 'Question21', 'Question22', 'Question23', 'Question24', 'Question25', 'Question26', 'Question27',
                 'Question28', 'Question29', 'Question30',
                 'Question31', 'Question32', 'Question33', 'Question34', 'Question35', 'Question36', 'Question37',
                 'Question38', 'Question39', 'Question40',
                 'D_result'])
            writer.writerow(
                Result.objects.values_list('Name', 'Question1', 'Question2', 'Question3', 'Question4', 'Question5',
                                           'Question6', 'Question7', 'Question8', 'Question9', 'Question10',
                                           'Question11', 'Question12', 'Question13', 'Question14', 'Question15',
                                           'Question16', 'Question17', 'Question18', 'Question19', 'Question20',
                                           'Question21', 'Question22', 'Question23', 'Question24', 'Question25',
                                           'Question26', 'Question27', 'Question28', 'Question29', 'Question30',
                                           'Question31', 'Question32', 'Question33', 'Question34', 'Question35',
                                           'Question36', 'Question37', 'Question38', 'Question39', 'Question40'
                                           ).order_by('-pk')[0])

            csvfile.close()

        return HttpResponseRedirect('after_test/')

    return render(request, 'index.html', {'form': form})


def after_test(request):
    review.analy.load_analy()
    time.sleep(5)
    template = loader.get_template("after_test.html")
    file = str(Result.objects.values_list('Name').order_by('-pk')[0])
    file = file.replace("'", "")
    CSV_PATH2 = 'after_analy' + file + '.csv'
    with open(CSV_PATH2, 'r', encoding='utf-8', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        next(reader)
        last_data = []
        for row in reader:
            last_data.append(row)
        csvfile.close()
        last_result = last_data[0][1]
        obj = Result.objects.order_by('-pk')[0]
        obj.voted = last_result
        obj.save()

        result = obj
    context = {
        'result': result

    }

    return HttpResponse(template.render(context, request))
