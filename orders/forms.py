from django import forms
from orders.models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['full_name', 'mobile', 'address', 'email', 'cnc_file', 'material', 'thickness']
        widgets = {
            'full_name': forms.TextInput(attrs={'placeholder': 'Enter your full name'}),
            'mobile': forms.TextInput(attrs={'placeholder': '09xxxxxxxxx', 'maxlength': '11'}),
            'address': forms.TextInput(attrs={'placeholder': 'Enter your address'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter your email'}),
            'cnc_file': forms.FileInput(),
            'material': forms.HiddenInput(),
            'thickness': forms.HiddenInput(),
        }

    def clean_mobile(self):
        mobile = self.cleaned_data['mobile']
        if not mobile:
            raise forms.ValidationError('Mobile number is required.')
        if not mobile.startswith('09') or not mobile.isdigit() or len(mobile) != 11:
            raise forms.ValidationError('Mobile number must start with "09" and be exactly 11 digits (e.g., 09123456789). No spaces or other characters allowed.')
        return mobile

    def clean_email(self):
        email = self.cleaned_data['email']
        if not email:
            raise forms.ValidationError('Email is required.')
        return email

    def clean_full_name(self):
        full_name = self.cleaned_data['full_name']
        if not full_name.strip():
            raise forms.ValidationError('Full name is required.')
        return full_name

    def clean_address(self):
        address = self.cleaned_data['address']
        if not address.strip():
            raise forms.ValidationError('Address is required.')
        return address

    def clean_cnc_file(self):
        cnc_file = self.cleaned_data['cnc_file']
        if not cnc_file:
            raise forms.ValidationError('A CNC file is required.')
        allowed_extensions = ['.nc', '.gcode', '.cnc', '.dxf', '.stl', '.step', '.stp', '.svg']
        if not any(cnc_file.name.lower().endswith(ext) for ext in allowed_extensions):
            raise forms.ValidationError('File must be one of: .nc, .gcode, .cnc, .dxf, .stl, .step, .stp, .svg')
        return cnc_file

    def clean_material(self):
        material = self.cleaned_data['material']
        if not material:
            raise forms.ValidationError('Material selection is required.')
        return material

    def clean_thickness(self):
        thickness = self.cleaned_data['thickness']
        if not thickness:
            raise forms.ValidationError('Thickness selection is required.')
        try:
            float(thickness)  # Allow decimal thicknesses (e.g., 0.3)
        except ValueError:
            raise forms.ValidationError('Thickness must be a number.')
        return thickness
