from django.shortcuts import render_to_response
from pages.models import entry

# A simple view to list all entries
def entries_index(request):
    return render_to_response('pages/entry_index.html',
                                  { 'entry_list': entry.objects.all() })