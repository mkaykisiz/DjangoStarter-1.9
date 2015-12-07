from django.contrib.auth.models import Group
from django.forms import Textarea
from Tangos.models import *
from adminpanel.models import Pages
from list.models import *
from orders.models import Cargo, PaymentSystem, CargoDesiPrice, InstallmentBankInfo, Installment, WebPosInfo, \
    TransferInfo

__author__ = 'kaykisizcom'

from django import forms


class NewCategoryForm(forms.ModelForm):
    class Meta:
        model = Categories
        fields = "__all__"
        widgets = {'seo_meta_description': Textarea(attrs={'cols': 80, 'rows': 7})}


class NewMenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = "__all__"
        widgets = {}


class NewAreaForm(forms.ModelForm):
    class Meta:
        model = Area
        fields = "__all__"
        widgets = {}


class NewCityForm(forms.ModelForm):
    class Meta:
        model = Cities
        fields = "__all__"
        widgets = {}


class NewCountyForm(forms.ModelForm):
    class Meta:
        model = Counties
        fields = "__all__"
        widgets = {}


class new_cargo_form(forms.ModelForm):
    class Meta:
        model = Cargo
        fields = "__all__"
        widgets = {}


class NewCargoDesiPriceForm(forms.ModelForm):
    class Meta:
        model = CargoDesiPrice
        fields = "__all__"
        widgets = {}


class NewInstallmentBankInfoForm(forms.ModelForm):
    class Meta:
        model = InstallmentBankInfo
        fields = "__all__"
        widgets = {}


class NewPaymentSystemForm(forms.ModelForm):
    class Meta:
        model = PaymentSystem
        fields = "__all__"
        widgets = {}


class NewWebPosInfoForm(forms.ModelForm):
    class Meta:
        model = WebPosInfo
        fields = "__all__"
        widgets = {}
        exclude = ('payment_system',)


class NewTransferInfoForm(forms.ModelForm):
    class Meta:
        model = TransferInfo
        fields = "__all__"
        widgets = {}
        exclude = ('payment_system',)


class NewInstallmentForm(forms.ModelForm):
    class Meta:
        model = Installment
        fields = "__all__"
        widgets = {'bank': forms.HiddenInput}


class new_features_form(forms.ModelForm):
    class Meta:
        model = Features
        fields = "__all__"
        widgets = {}


class new_productdetails_form(forms.ModelForm):
    class Meta:
        model = ProductDetails
        fields = "__all__"
        widgets = {}


class new_categoriesandfeatures_form(forms.ModelForm):
    class Meta:
        model = CategoriesAndFeatures
        fields = "__all__"
        widgets = {}


class new_optionalfeatures_form(forms.ModelForm):
    class Meta:
        model = OptionalFeatures
        fields = "__all__"
        widgets = {}


class new_optionaldetails_form(forms.ModelForm):
    class Meta:
        model = OptionalDetails
        fields = "__all__"
        widgets = {}


class update_user_profile_form(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"
        widgets = {'last_login': forms.HiddenInput,
                   'is_superuser': forms.HiddenInput,
                   'username': forms.HiddenInput,
                   'is_staff': forms.HiddenInput,
                   'date_joined': forms.HiddenInput,
                   'is_active': forms.HiddenInput,
                   'groups': forms.HiddenInput,
                   'user_permissions': forms.HiddenInput,
                   'password': forms.HiddenInput
                   }


class new_brand_form(forms.ModelForm):
    class Meta:
        model = Brand
        fields = "__all__"
        widgets = {}


class new_brand_and_category_form(forms.ModelForm):
    class Meta:
        model = BrandAndCategories
        fields = "__all__"
        widgets = {}


class new_money_type_form(forms.ModelForm):
    class Meta:
        model = MoneyType
        fields = "__all__"
        widgets = {}


class new_advertising_form(forms.ModelForm):
    class Meta:
        model = Advertising
        fields = "__all__"
        widgets = {}


class new_hr_form(forms.ModelForm):
    class Meta:
        model = HumanResources
        fields = "__all__"
        widgets = {'address': Textarea(attrs={'cols': 80, 'rows': 3})}


class new_contact_form(forms.ModelForm):
    class Meta:
        model = Contacts
        fields = "__all__"
        widgets = {}


class new_specialshowcase_form(forms.ModelForm):
    class Meta:
        model = SpecialShowcase
        fields = "__all__"
        widgets = {}


class NewProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = "__all__"
        widgets = {'user': forms.HiddenInput,
                   'description': Textarea(attrs={'cols': 80, 'rows': 7}),
                   'long_description': Textarea(attrs={'cols': 80, 'rows': 13}),
                   'seo_meta_keyword': Textarea(attrs={'cols': 80, 'rows': 7}),
                   'seo_meta_description': Textarea(attrs={'cols': 80, 'rows': 7}),
                   'avg_point': forms.HiddenInput,
                   'sequence_no': forms.HiddenInput,
                   'category': forms.HiddenInput}


class add_product_photos_form(forms.ModelForm):
    class Meta:
        model = ProductsPhoto
        fields = "__all__"
        widgets = {'product': forms.HiddenInput}


class add_company_price_form(forms.ModelForm):
    class Meta:
        model = CompanyPrice
        fields = "__all__"
        widgets = {'product': forms.HiddenInput}


class new_optional_for_company_form(forms.ModelForm):
    class Meta:
        model = CompanyOptionalPrice
        fields = "__all__"
        widgets = {'product': forms.HiddenInput}



class new_dijital_form(forms.ModelForm):
    class Meta:
        model = ProductDigital
        fields = "__all__"
        widgets = {'is_used': forms.HiddenInput,
                   'product': forms.HiddenInput}


class new_message_form(forms.ModelForm):
    class Meta:
        model = MessageContents
        fields = "__all__"
        widgets = {'message': forms.HiddenInput,
                   'user': forms.HiddenInput}


class update_user_form(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"
        widgets = {'last_login': forms.HiddenInput,
                   'is_superuser': forms.HiddenInput,
                   'is_staff': forms.HiddenInput,
                   'date_joined': forms.HiddenInput,
                   'groups': forms.HiddenInput,
                   'password': forms.HiddenInput,
                   'user_permissions': forms.HiddenInput
                   }


class update_users_form(forms.ModelForm):
    class Meta:
        model = Users
        fields = "__all__"
        widgets = {'user': forms.HiddenInput,
                   'group': forms.ChoiceField,
                   'profile_photo': forms.HiddenInput}


class update_company_form(forms.ModelForm):
    class Meta:
        model = Companies
        fields = "__all__"
        widgets = {'user': forms.HiddenInput,
                   'profile_photo': forms.HiddenInput}


class new_page_form(forms.ModelForm):
    class Meta:
        model = Pages
        fields = "__all__"
        widgets = {}


class new_group_form(forms.ModelForm):
    class Meta:
        model = Group
        fields = "__all__"
        widgets = {}


class new_company_settings_form(forms.ModelForm):
    class Meta:
        model = CompanySettings
        fields = "__all__"
        widgets = {'address': Textarea(attrs={'cols': 80, 'rows': 7}),
                   }


class new_footer_form(forms.ModelForm):
    class Meta:
        model = Footer
        fields = "__all__"
        widgets = {}


class new_Project_settings_form(forms.ModelForm):
    class Meta:
        model = ProjectSettings
        fields = "__all__"
        widgets = {'user_home_panel': Textarea(attrs={'cols': 80, 'rows': 7}),
                   'company_home_panel': Textarea(attrs={'cols': 80, 'rows': 7}),
                   'seo_title': Textarea(attrs={'cols': 80, 'rows': 7}),
                   'seo_meta_keyword': Textarea(attrs={'cols': 80, 'rows': 7}),
                   'seo_meta_description': Textarea(attrs={'cols': 80, 'rows': 7}),
                   'refund_conditions': Textarea(attrs={'cols': 80, 'rows': 7}),
                   'membership_agreement': Textarea(attrs={'cols': 80, 'rows': 7}),
                   }