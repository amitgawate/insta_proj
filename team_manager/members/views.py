from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import redirect
from django.contrib import messages
from .models import TeamMember
from .forms import TeamMemberForm

class TeamMemberListView(ListView):
    model = TeamMember
    template_name = 'members/team_member_list.html'
    context_object_name = 'team_members'

class TeamMemberCreateView(CreateView):
    model = TeamMember
    form_class = TeamMemberForm
    template_name = 'members/team_member_form.html'
    success_url = reverse_lazy('team_member_list')

class TeamMemberUpdateView(UpdateView):
    model = TeamMember
    form_class = TeamMemberForm
    template_name = 'members/team_member_form.html'
    success_url = reverse_lazy('team_member_list')

class TeamMemberDeleteView(DeleteView):
    model = TeamMember
    template_name = 'members/team_member_confirm_delete.html'
    success_url = reverse_lazy('team_member_list')

    def dispatch(self, request, *args, **kwargs):
        member = self.get_object()
        if member.role == 'admin':
            messages.error(request, 'Admin users cannot be deleted.')
            return redirect('team_member_list')
        return super().dispatch(request, *args, **kwargs)
