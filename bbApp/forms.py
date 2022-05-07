from random import choices
import sched
from django import forms
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm, UserChangeForm

from django.contrib.auth.models import User
from bbApp import models
from datetime import datetime

class UpdateProfile(UserChangeForm):
    username = forms.CharField(max_length=250,help_text="The Username field is required.")
    email = forms.EmailField(max_length=250,help_text="The Email field is required.")
    first_name = forms.CharField(max_length=250,help_text="The First Name field is required.")
    last_name = forms.CharField(max_length=250,help_text="The Last Name field is required.")
    current_password = forms.CharField(max_length=250)

    class Meta:
        model = User
        fields = ('email', 'username','first_name', 'last_name')

    def clean_current_password(self):
        if not self.instance.check_password(self.cleaned_data['current_password']):
            raise forms.ValidationError(f"Password is Incorrect")

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            user = User.objects.exclude(id=self.cleaned_data['id']).get(email = email)
        except Exception as e:
            return email
        raise forms.ValidationError(f"The {user.email} mail is already exists/taken")

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            user = User.objects.exclude(id=self.cleaned_data['id']).get(username = username)
        except Exception as e:
            return username
        raise forms.ValidationError(f"The {user.username} mail is already exists/taken")

class UpdatePasswords(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control form-control-sm rounded-0'}), label="Old Password")
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control form-control-sm rounded-0'}), label="New Password")
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control form-control-sm rounded-0'}), label="Confirm New Password")
    class Meta:
        model = User
        fields = ('old_password','new_password1', 'new_password2')

class SaveBloodGroup(forms.ModelForm):
    name = forms.CharField(max_length="250")
    status = forms.ChoiceField(choices=[('1','Active'),('2','Inctive')])

    class Meta:
        model = models.Blood_Group
        fields = ('name', 'status',)


class SaveDonation(forms.ModelForm):
    blood_group = forms.CharField(max_length="500", label="Blood Group")
    donor_name = forms.CharField(max_length="500", label="Donor's Name")
    donor_contact = forms.CharField(max_length="250", label="Donor's Contact")
    donor_email = forms.CharField(max_length="250", label="Donor's Email")
    donor_gender = forms.ChoiceField(choices=[('Male','Male'),('Female','Female')], label="Donor's Gender")
    donor_address = forms.CharField(max_length=1000, label="Donor's Address")
    transfusion_date = forms.DateField(label="Transfusion Date")
    donation_volume = forms.CharField(max_length=100, label="Blood Volume")

    class Meta:
        model = models.Donation
        fields = ('blood_group', 'donor_name', 'donor_contact', 'donor_email', 'donor_gender', 'donor_address', 'transfusion_date', 'donation_volume',)
    
    def clean_blood_group(self):
        bgID = self.cleaned_data['blood_group']
        bgID = bgID if bgID.isnumeric() else 0
        try:
            blood_group = models.Blood_Group.objects.get(id=bgID)
            return blood_group
        except:
            raise forms.ValidationError("Invalid Selected Blood Group")

class SaveRequest(forms.ModelForm):
    blood_group = forms.CharField(max_length="500", label="Blood Group")
    physician_name = forms.CharField(max_length="500", label="Patient's Name")
    patient_name = forms.CharField(max_length="500", label="Patient's Name")
    patient_gender = forms.ChoiceField(choices=[('Male','Male'),('Female','Female')], label="Patient's Gender")
    status = forms.ChoiceField(choices = [('1' ,'Pending'),('2' ,'Approved'),('3' ,'Handed-Over'),('4' ,'Denied')], label="Status")
    volume = forms.CharField(max_length=100, label="Blood Volume")

    class Meta:
        model = models.Request
        fields = ('blood_group', 'patient_name', 'patient_gender', 'status', 'volume','physician_name',)
    
    def clean_blood_group(self):
        bgID = self.cleaned_data['blood_group']
        bgID = bgID if bgID.isnumeric() else 0
        try:
            blood_group = models.Blood_Group.objects.get(id=bgID)
            return blood_group
        except:
            raise forms.ValidationError("Invalid Selected Blood Group")
        
