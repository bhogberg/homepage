from django.shortcuts import render_to_response
from entries.models import entry

# A simple view to list all entries
def entries_index(request):
    return render_to_response('entry_index.html',
                                  { 'entry_list': entry.objects.all() })