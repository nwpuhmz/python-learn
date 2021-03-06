from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from polls.models import Poll
from django.template import Context,loader
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse
# Create your views here.

# def index(request):
#     latest_poll_list = Poll.objects.order_by("-pub_date")[:5]
#     template = loader.get_template("polls/index.html")
#     context = Context({
#         'latest_poll_list':latest_poll_list,
#         })
#     return HttpResponse(template.render(context))

# def detail(request, poll_id):
#     try:
#         poll = Poll.objects.get(pk=poll_id)
#     except Poll.DoesNotExist:
#         raise Http404
#     return render(request, 'polls/detail.html', {'poll': poll})

# def results(request, poll_id):
#     poll = get_object_or_404(Poll,pk=poll_id)
#     return render(request,'polls/results.html',{'poll':poll})

def vote(request, poll_id):
    p = get_object_or_404(Poll,pk=poll_id)
    try:
        selected_choice = p.choice_set.get(pk= request.POST['choice'])
    except (KeyError,Choice.DoesNotExist):
        return render(request,'polls/detail.html',{'poll':p,'error_message':"You didn't select a choice.",})
    else:
        selected_choice.votes+=1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results',args=(p.id,)))

