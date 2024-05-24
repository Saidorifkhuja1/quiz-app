
from django.contrib.auth import login
from django.views.generic import CreateView, FormView
from .forms import CustomerCreationForm
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy
from .forms import AccountSettingsForm, EmailPreferencesForm, DeleteAccountForm




class SignupView(CreateView):
    form_class = CustomerCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        # Save the form data and create the user
        user = form.save()

        # Log in the user after successful registration
        login(self.request, user)

        # Redirect to appropriate page based on user role (teacher or student)
        if user.are_you_teacher:
            return redirect('home')  # Replace 'teacher_dashboard' with your URL name for teacher dashboard
        else:
            return redirect('home')  # Replace 'student_dashboard' with your URL name for student dashboard

    def form_invalid(self, form):
        # If the form is invalid, re-render the signup page with the form and errors
        return self.render_to_response(self.get_context_data(form=form))
class AccountSettingsView(FormView):
    template_name = 'settings.html'
    form_class = AccountSettingsForm
    success_url = reverse_lazy('settings')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        email_prefs_form = EmailPreferencesForm(instance=user)
        delete_account_form = DeleteAccountForm()
        context['email_prefs_form'] = email_prefs_form
        context['delete_account_form'] = delete_account_form
        return context

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Your profile was successfully updated!')
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        email_prefs_form = EmailPreferencesForm(request.POST, instance=request.user)
        delete_account_form = DeleteAccountForm(request.POST)

        if email_prefs_form.is_valid():
            email_prefs_form.save()
            messages.success(request, 'Your email preferences were updated!')
            return redirect('settings')

        elif delete_account_form.is_valid() and delete_account_form.cleaned_data['confirm_deletion']:
            request.user.delete()
            messages.success(request, 'Your account has been deleted.')
            return redirect('home')  # Redirect to home or login page after deletion

        return super().post(request, *args, **kwargs)


