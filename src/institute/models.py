import os
from django.db import models
from django.core.validators import RegexValidator, validate_email
from django.core.exceptions import ValidationError
from django.utils.encoding import smart_unicode
from django.template.defaultfilters import slugify

#media root dirs.
MEDIA_ROOT_IMAGES = 'images/'
MEDIA_ROOT_GALLERY = 'gallery/'
MEDIA_ROOT_DOCUMENTS = 'documents/'

#Function for saving images/docs in dynamic path. 


def __get_path_faculty__(instance, filename):
    getDept = instance.dept.dept_code
    upload_dir = os.path.join(MEDIA_ROOT_IMAGES,getDept,'Faculty')
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)
    return os.path.join(upload_dir, filename)

def __get_path_notif__(instance, filename):
    upload_dir = os.path.join(MEDIA_ROOT_DOCUMENTS,instance.notif_of)
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)
    return os.path.join(upload_dir, filename)

def __get_path_gallery__(instance, filename):
    galleryId = instance.gallery_id.gallery_id
    galleryOf = instance.gallery_id.gallery_of
    galleryTitle = instance.gallery_id.gallery_title
    upload_dir = os.path.join(MEDIA_ROOT_GALLERY,galleryOf,'%s_%s'%(galleryId,galleryTitle))
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)
    return os.path.join(upload_dir, filename)

def __get_path_seminars__(instance, filename):
    upload_dir = os.path.join(MEDIA_ROOT_DOCUMENTS,'Seminars & Conferences')
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)
    return os.path.join(upload_dir, filename)

def __get_path_tenders__(instance, filename):
    upload_dir = os.path.join(MEDIA_ROOT_DOCUMENTS,'Tenders')
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)
    return os.path.join(upload_dir, filename)

def __get_path_committees__(instance, filename):
    upload_dir = os.path.join(MEDIA_ROOT_DOCUMENTS,'Committees')
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)
    return os.path.join(upload_dir, filename)

def __get_path_directors__(instance, filename):
    getRankName = instance.rank_id.rank_name
    upload_dir = os.path.join(MEDIA_ROOT_IMAGES,'Directors & Deans',getRankName)
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)
    return os.path.join(upload_dir, filename)

def __get_path_rti__(instance,filename):
    upload_dir = os.path.join(MEDIA_ROOT_DOCUMENTS,'RTI')
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)
    return os.path.join(upload_dir,filename)

def __get_path_calendar__(instance,filename):
    upload_dir = os.path.join(MEDIA_ROOT_DOCUMENTS,'Calendar')
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)
    return os.path.join(upload_dir,filename)

def __get_path_cir__(instance,filename):
    upload_dir = os.path.join(MEDIA_ROOT_DOCUMENTS,'Curricular')
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)
    return os.path.join(upload_dir,filename)

def __get_path_wmes__(instance, filename):
    upload_dir = os.path.join(MEDIA_ROOT_DOCUMENTS,'WMES')
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)
    return os.path.join(upload_dir,filename)

def __get_path_newent__(instance, filename):
    upload_dir = os.path.join(MEDIA_ROOT_DOCUMENTS,'NewEntrants')
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)
    return os.path.join(upload_dir,filename)

def __get_path_admdoc__(instance, filename):
    upload_dir = os.path.join(MEDIA_ROOT_DOCUMENTS,'AdmissionDoc')
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)
    return os.path.join(upload_dir,filename)

def __get_path_feedoc__(instance, filename):
    upload_dir = os.path.join(MEDIA_ROOT_DOCUMENTS,'FeeStructure')
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)
    return os.path.join(upload_dir,filename)

def __get_path_orddoc__(instance, filename):
    upload_dir = os.path.join(MEDIA_ROOT_DOCUMENTS,'Ordinance')
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)
    return os.path.join(upload_dir,filename)

def __get_path_schdoc__(instance, filename):
    upload_dir = os.path.join(MEDIA_ROOT_DOCUMENTS,'ScholarShip')
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)
    return os.path.join(upload_dir,filename)

def __get_path_convo__(instance, filename):
    upload_dir = os.path.join(MEDIA_ROOT_DOCUMENTS,'Convocation')
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)
    return os.path.join(upload_dir,filename)

def __get_path_cerd__(instance, filename):
    upload_dir = os.path.join(MEDIA_ROOT_DOCUMENTS,'CERD')
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)
    return os.path.join(upload_dir,filename)


# Create your models here.

alphanum = RegexValidator(r'^[0-9 a-z A-Z]*$','Only Alphanumeric values are allowed')
num = RegexValidator(r'^[0-9]*$','Only Integer values are allowed')
tenDigitContact = RegexValidator(r'^\d{10,10}$','Enter a Valid 10 digit number.', 'Invalid number')
emailValidation = RegexValidator(r'^[0-9_ a-z A-Z \-\.]+(@iitbhu\.ac\.in|@itbhu\.ac\.in)*$')
INITIAL = 1


class Department(models.Model):
    dept_code = models.CharField(unique=True, max_length = 2, primary_key = True, blank = False)
    dept_name = models.CharField(max_length = 50, blank=False, null=True)
    contact1 = models.IntegerField(null = True, blank = True, validators=[tenDigitContact])
    contact2 = models.IntegerField(null = True, blank = True, validators=[tenDigitContact])

    def __unicode__(self):
        return smart_unicode(self.dept_code)+' : '+smart_unicode(self.dept_name)


class Faculty(models.Model):
    name = models.CharField(max_length = 50, blank = False)
    dept = models.ForeignKey(Department, blank=False)
    photo = models.ImageField(upload_to = __get_path_faculty__, default = 'null')
    designation = models.CharField(max_length = 20, null = True, blank = True)
    qualification = models.CharField(max_length = 100, null = True, blank = True)
    area_of_interest = models.CharField(max_length = 100, null = True, blank = True)
    contact_off = models.IntegerField(null = True, blank = True, validators=[tenDigitContact])
    contact_res = models.IntegerField(null = True, blank = True, validators=[tenDigitContact])
    contact_other = models.IntegerField(null = True, blank = True, validators=[tenDigitContact])
    email_off = models.EmailField(unique = True, null = False, blank = False, validators = [emailValidation],
                                  error_messages = {'invalid':'Enter your Official Email-ID.'})
    email_other = models.EmailField(unique = True,null = True, blank =True, default = None)
    #Available/Out of Station/On Leave
    status = models.CharField(max_length = 10, null = True, blank = True)
    faculty_id = models.CharField(unique=True, max_length =100, primary_key = True, editable = False)

    def save(self, *args, **kwargs):
        if not self.faculty_id:
            self.faculty_id = self.email_off.split('@')[0]
        super(Faculty,self).save(*args,**kwargs)
        #returns a none value for an empty string if the email field is left blank.
        if self.email_other == "":
            self.email_other = None
        super(Faculty,self).save(*args, **kwargs)

    def __unicode__(self):
        return smart_unicode(self.name)+' : '+smart_unicode(self.email_off)+' : '+smart_unicode(self.faculty_id)


class Student(models.Model):
    # ENGG_YEAR = {
    #     (1,'1st Yr'),
    #     (2,'2nd Yr'),
    #     (3,'3rd Yr'),
    #     (4,'4th Yr'),
    #     (5,'5th Yr'),
    # }
    DEGREE = {
            (1,'B.Tech'),
            (2,'IDD'),
            (3,'M.Tech'), 
    }
    roll_no = models.CharField(unique = True, max_length = 20, primary_key = True, blank = False, validators=[alphanum])
    name = models.CharField(max_length = 50, null = False, blank = False)
    year_of_admission = models.IntegerField(null = False, blank = False, default = 0, editable = False)
    degree = models.IntegerField(choices = DEGREE, default = 1)
    email = models.EmailField(unique = True, null = False, blank = False, validators = [emailValidation],
                              error_messages = {'invalid':'Enter your Official Email-ID.'})
    dept = models.ForeignKey(Department)

    def save(self,*args,**kwargs):
        #extract year from email.
        self.year_of_admission = int((self.email.split('@')[0])[-2:])
        super(Student,self).save(*args,**kwargs)
    def __unicode__(self):
        return smart_unicode(self.roll_no)+' : '+smart_unicode(self.name)


class Phd(models.Model):
    name = models.CharField(max_length = 50, null = False, blank = False)    
    dept = models.ForeignKey(Department)
    supervisor = models.CharField(max_length = 50, null = True, blank = True)
    co_supervisor = models.CharField(max_length = 50, null = True, blank = True)


class PhdResearch(models.Model):
    name = models.CharField(max_length = 50, null = False, blank = False)    
    dept = models.ForeignKey(Department)
    supervisor = models.CharField(max_length = 50, null = True, blank = True)
    topic = models.CharField(max_length = 200, null = False, blank = False)    
    status = models.CharField(max_length = 50, null = False, blank = False)    

class Staff(models.Model):
    name = models.CharField(max_length = 50, null = False, blank = False)
    dept = models.ForeignKey(Department, null = False, blank = False)
    designation = models.CharField(max_length = 20, null = False, blank = False)
    email = models.EmailField()

    def save(self, *args, **kwargs):
        if self.email == "":
            self.email = None
        super(Faculty,self).save(*args, **kwargs)

    def __unicode__(self):
        return smart_unicode(self.name)+' : '+smart_unicode(self.email)


class Groups(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    short = models.CharField(max_length=10, unique=True, blank=False, null=False)
    description = models.CharField(max_length=250, blank=True, null=True)

    def __unicode__(self):
        return smart_unicode(self.short) + ' : ' + smart_unicode(self.name)


class Post(models.Model):
    PEOPLE = {
            ('1','Faculty'),
            ('2','Student'),
            ('3','Staff'),
            ('4','Others'),
    }
    name = models.CharField(max_length=50)
    group = models.ForeignKey(Groups)
    post_hold_by = models.CharField(max_length=5, choices=PEOPLE)

    def __unicode__(self):
        return smart_unicode(self.name) + " : " + smart_unicode(self.group)


class StudentsPost(models.Model):
    post = models.ForeignKey(Post)
    roll_no = models.CharField(max_length = 20, blank = False, validators=[alphanum])


class FacultiesPost(models.Model):
    post = models.ForeignKey(Post)
    dept = models.ForeignKey(Department)
    faculty = models.ForeignKey(Faculty)

class StaffsPost(models.Model):
    post = models.ForeignKey(Post)
    employee_id = models.CharField(max_length = 20, blank = False, validators=[alphanum])


class Notification(models.Model):
    PRIORITY_CHOICES = {
        (1,'High'),
        (2,'Normal'),
        (3,'Low'),
    }
    Qualtiy_CHOICES = {
        (1,'new'),
        (0,'old'),
    }
    notif_id = models.CharField(max_length = 30, primary_key = True)
    #lower the value = Higher the priority
    priority = models.IntegerField(choices = PRIORITY_CHOICES, default = 3)
    quality = models.IntegerField(choices = Qualtiy_CHOICES, default = 1)
    #notification of Institute or so and so department(department code).
    notif_of = models.CharField(max_length = 10, null = False, blank = False)
    title = models.CharField(max_length = 100, null = False, blank = False)
    desc = models.CharField(max_length = 100, null = True, blank = True)
    notif_doc = models.FileField(upload_to = __get_path_notif__, default = 'null')
    date = models.DateTimeField(auto_now_add = True, auto_now = False)
    slug = models.SlugField(max_length = 100, unique=True)

    def save(self,*args,**kwargs):
        if not self.notif_id:
            self.slug = slugify(self.title)
        super(Notification,self).save(*args,**kwargs)
    # def save(self,*args,**kwargs):
    #     self.slug = slugify(self.title)
    #     super(Notification,self).save(*args,**kwargs)

    # # def get_absolute_url(self):
    # #     return "/notification/%s/" % self.slug

    def __unicode__(self):
        return smart_unicode(self.notif_id)+' : '+smart_unicode(self.title)+' : '+smart_unicode(self.slug)


class Course(models.Model):
    COURSE_TYPE = {
        (1,'Theory'),
        (2,'Practical'),
    }
    course_id = models.IntegerField()
    sem = models.IntegerField()
    course_code = models.CharField(max_length = 10, null = False, blank = False, default = 'null')
    course_name = models.CharField(max_length = 50, null = False, blank = False, default = 'null')
    credits = models.IntegerField(default = 0)
    contact_hours = models.IntegerField(default = 0)
    #Theory/Practical
    type = models.IntegerField(choices = COURSE_TYPE, default = 1)
    #Value = 1 for the appropriate degree
    b_tech = models.IntegerField(default = 0)
    idd = models.IntegerField(default = 0)
    m_tech = models.IntegerField(default = 0)
    ph_d = models.IntegerField(default = 0)
    dept = models.CharField(max_length = 3, null = False, blank = False)
    course_offered_by = models.CharField(max_length = 3, null = False, blank = False)

    def __unicode__(self):
        return smart_unicode(self.course_id)+' : '+smart_unicode(self.course_name)


class Gallery(models.Model):
    gallery_id = models.CharField(max_length = 30, primary_key = True, blank = False)
    #Institute or Dept_code
    gallery_of = models.CharField(max_length = 50, null = True, blank = True)
    gallery_title = models.CharField(max_length = 50, null = True, blank = True)
    gallery_desc = models.CharField(max_length = 100, null = True, blank = True)
    upload_date = models.DateTimeField(auto_now_add = True, auto_now = False)
    
    def __unicode__(self):
        return smart_unicode(self.gallery_id)+' : '+smart_unicode(self.gallery_title)


class Image(models.Model):
    gallery_id = models.ForeignKey(Gallery)
    img_id = models.CharField(max_length = 30, primary_key = True, blank = False)
    img_caption = models.CharField(max_length = 50, null = True, blank = True)
    img = models.ImageField(upload_to = __get_path_gallery__, default = 'null')
    upload_date = models.DateTimeField(auto_now_add = True, auto_now = False)

    def __unicode__(self):
        return smart_unicode(self.img_id)+' : '+smart_unicode(self.img_caption)


#Institute
class SeminarsConf(models.Model):
    title = models.CharField(max_length = 50, null = False, blank = False)
    desc = models.CharField(max_length = 100, null = True, blank = True)
    doc = models.FileField(upload_to = __get_path_seminars__)
    date = models.CharField(max_length = 20, null = True, blank = True)
    time = models.CharField(max_length = 10, null = True, blank = True)
    venue = models.CharField(max_length = 50, null = True, blank = True)

    def __unicode__(self):
        return smart_unicode(self.title)


class Event(models.Model):
    event_name = models.CharField(max_length = 100, null = True, blank = True)
    event_dt = models.CharField(max_length = 100, null = True, blank = True)
    event_venue = models.CharField(max_length = 100, null = True, blank = True)
    event_desc = models.CharField(max_length = 100, null = True, blank = True)

    def __unicode__(self):
        return smart_unicode(self.event_name)


class Tender(models.Model):
    tender_id = models.CharField(max_length = 100, null = True, blank = True)
    dept = models.CharField(max_length = 100, null = True, blank = True)
    posting_dt = models.CharField(max_length = 100, null = True, blank = True)
    closing_dt = models.CharField(max_length = 100, null = True, blank = True)
    desc = models.CharField(max_length = 100, null = True, blank = True)

    def __unicode__(self):
        return smart_unicode(self.tender_id)


class TenderDoc(models.Model):
    tender_id = models.CharField(max_length = 100, null = True, blank = True)
    tender_name = models.CharField(max_length = 100, null = True, blank = True)
    tender_doc = models.FileField(upload_to = __get_path_tenders__)

    def __unicode__(self):
        return smart_unicode(self.tender_name)

"""
class Committee(models.Model):
    comm_id = models.IntegerField(primary_key = True, blank = False)
    comm_related_to = models.CharField(max_length = 100, null = True, blank = True)

    def __unicode__(self):
        return smart_unicode(self.comm_related_to)
"""


class CommDetail(models.Model):
    comm_id = models.IntegerField(null = False, blank = False)
    comm_for = models.CharField(max_length = 100, null = True, blank = True)
    notif_no = models.CharField(max_length = 100, null = True, blank = True)
    dated = models.CharField(max_length = 100, null = True, blank = True)
    comm_doc = models.FileField(upload_to = __get_path_committees__, default = 'null')
    comm_img = models.ImageField(upload_to = __get_path_committees__, default = 'null')

    def __unicode__(self):
        return smart_unicode(self.notif_no)


class AdminOfficial(models.Model):
    rank_id = models.IntegerField(null = False, blank = False)
    name = models.CharField(max_length = 100, null = True, blank = True)
    rank_area = models.CharField(max_length = 100 , blank = True)
    qualification = models.CharField(max_length = 100, null = True, blank = True)
    contact_off = models.IntegerField(null = True, blank = True, validators=[tenDigitContact])
    contact_res = models.IntegerField(null = True, blank = True, validators=[tenDigitContact])
    contact_other = models.IntegerField(null = True, blank = True, validators=[tenDigitContact])
    email_off = models.EmailField(unique = True, null = True, blank = True, validators = [emailValidation],
                                  error_messages = {'invalid':'Enter your Official Email-ID.'})
    email_other = models.EmailField(unique = True, null = True, blank = True)
    fax = models.IntegerField(null = True, blank = True)

    def save(self, *args, **kwargs):
        if self.email_other == "":
            self.email_other = None
        super(Faculty,self).save(*args, **kwargs)

    def __unicode__(self):
        return smart_unicode(self.name)


class BoardOfGovernor(models.Model):
    level = models.CharField(max_length = 100, null = True, blank = True)
    name = models.CharField(max_length = 100, null = True, blank = True)
    rank = models.CharField(max_length = 100, null = True, blank = True)
    address = models.CharField(max_length = 100, null = True, blank = True)

    def __unicode__(self):
        return smart_unicode(self.level)+' : '+smart_unicode(self.name)+' : '+smart_unicode(self.rank)

"""
class HostelAdmin(models.Model):
    hostel = models.CharField(max_length = 100, null = True, blank = True)
    admin_war = models.CharField(max_length = 100, null = True, blank = True)
    war1 = models.CharField(max_length = 100, null = True, blank = True)
    war2 = models.CharField(max_length = 100, null = True, blank = True)
    email_admin = models.EmailField(unique = True, null = True, blank = True)
    email_war1 = models.EmailField(unique = True, null = True, blank = True)
    email_war2 = models.EmailField(unique = True, null = True, blank = True)

    def save(self, *args, **kwargs):
        if self.email_admin == "":
            self.email_admin = None
        super(Faculty,self).save(*args, **kwargs)
        if self.email_war1 == "":
            self.email_war1 = None
        super(Faculty,self).save(*args, **kwargs)
        if self.email_war2 == "":
            self.email_war2 = None
        super(Faculty,self).save(*args, **kwargs)

    def __unicode__(self):
        return smart_unicode(self.hostel)
"""

class Security(models.Model):
    name = models.CharField(max_length =100, null =  True , blank = True)
    designation = models.CharField(max_length = 100 ,null = True , blank = True)
    contact = models.IntegerField(null= True , blank = True , validators=[tenDigitContact])

    def __unicode__(self):
        return smart_unicode(self.name)

class HeadOfDepartments(models.Model):
    department = models.ForeignKey(Department , blank=False)
    name = models.ForeignKey(Faculty)
    
    def __unicode__(self):
        return smart_unicode(self.department)

class RightToInformation(models.Model):
    info_reg = models.CharField(null = True , blank = True , max_length = 300)
    description = models.CharField(null=True,blank= True , max_length = 300)
    rti_doc = models.FileField(upload_to = __get_path_rti__ , default = 'null')
    
    def __unicode__(self):
        return smart_unicode(self.info_reg)

class Calendar(models.Model):
    sem_name = models.CharField(max_length = 100 , blank = True)
    sem_type = models.CharField(max_length = 4)
    registration_date = models.DateField()
    calendar_doc = models.FileField(upload_to = __get_path_calendar__, default = 'null')
    sem_comnc_date = models.DateField(auto_now_add = False,  auto_now = False )
    sem_reg_date   = models.DateField(auto_now_add = False ,  auto_now = False)
    
    
    def __unicode__(self):
        return smart_unicode(self.sem_name)

class Circulars(models.Model):
    title = models.CharField(max_length = 100)
    ref_no = models.CharField(blank = True , max_length = 100)
    date = models.DateField(null = True)
    cir_doc = models.FileField(upload_to = __get_path_cir__ , default = 'null')
    
    def __unicode__(self):
        return smart_unicode(self.title)
"""
class Wmes(models.Model):
    desig = models.CharField(max_length = 100 ,blank =True)
    name  = models.CharField(max_length = 100 , blank =False , null = False)
    email = models.EmailField(unique = True , blank = False , null = False)
    linked_in = models.CharField(max_length = 200 ,unique = True , blank = True)
    dept  = models.CharField(blank = False , null = False , max_length = 100)
    mem_type = models.CharField(max_length = 100 , blank = False , null = False)
    prof_pic = models.FileField(upload_to = __get_path_wmes__ , default = 'null')
    
    def __unicode__(self):
        return smart_unicode(self.name)    
"""

class NewsBoard(models.Model):
    news_of = models.CharField(max_length = 20 , blank = False , null = False)
    title = models.CharField(max_length = 200)
    descr = models.TextField(blank  = True)
    date =  models.DateField(null = False)
    
    def __unicode__(self):
        return smart_unicode(self.title)
    
    
class NewEntrants(models.Model):
    title = models.CharField(max_length= 100 , blank = False , null = False)
    date  = models.DateField()
    ne_doc = models.FileField(upload_to = __get_path_newent__ ,default= 'null')
    
    def __unicode__(self):
        return smart_unicode(self.title)
    
class Admission(models.Model):
    admin_in_course = models.CharField(max_length = 100,null = False , blank = True)
    title = models.CharField(max_length = 300, blank = False , null= False)
    adm_doc = models.FileField(upload_to = __get_path_admdoc__ ,default = 'null')
    
    def __unicode__(self):
        return smart_unicode(self.title)

class FeeStructure(models.Model):
    fee_from_year = models.CharField(max_length = 100)
    fee_for = models.CharField(max_length = 100)
    fee_doc = models.FileField(upload_to = __get_path_feedoc__,default = 'null')
    
    def __unicode__(self):
        return smart_unicode(self.fee_for)

class TypeOfAcademicProgrammes(models.Model):
    name  = models.CharField(max_length= 100 , blank =False)
    degree = models.CharField(max_length= 100, blank= False , null = False)
    duration = models.IntegerField()
    adm_through = models.CharField(max_length = 10)
    no_of_progs = models.IntegerField()
    
    def __unicode__(self):
        return smart_unicode(self.name)
    
class Programmes(models.CharField):
    degree = models.ForeignKey(TypeOfAcademicProgrammes)
    name   = models.CharField(max_length = 100)
    Area_1   = models.CharField(max_length = 200 , blank = True )
    Area_2   = models.CharField(max_length = 200 , blank = True )
    Area_3   = models.CharField(max_length = 200 , blank = True )
    Area_4   = models.CharField(max_length = 200 , blank = True )
    Area_5   = models.CharField(max_length = 200 , blank = True )
    Area_6   = models.CharField(max_length = 200 , blank = True )
    Area_7   = models.CharField(max_length = 200 , blank = True )
    Area_8   = models.CharField(max_length = 200 , blank = True )
    Area_9   = models.CharField(max_length = 200 , blank = True )
    Area_10   = models.CharField(max_length = 200 , blank = True )
    Area_11  = models.CharField(max_length = 200 , blank = True )
    def __unicode__(self):
        return smart_unicode(self.name)

    

class Ordinance(models.Model):
    ordinance_type = models.CharField(max_length = 50)
    title = models.CharField(max_length = 100)
    ord_doc = models.FileField(upload_to = __get_path_orddoc__ , default = 'null')
    
    def __unicode__(self):
        return smart_unicode(self.title)



class ScholarShip(models.Model):
    title = models.CharField(max_length= 100)
    date  = models.DateField()
    scolar_doc = models.FileField(upload_to= __get_path_schdoc__ , default = 'null')
    
    def __unicode__(self):
        return smart_unicode(self.title)


class Convo(models.Model):
    title = models.CharField(max_length = 300)
    description = models.TextField()
    letter  = models.FileField(upload_to = __get_path_convo__ ,default = 'null')
    Form    = models.FileField(upload_to = __get_path_convo__ , default = 'null') 
    schedule = models.FileField(upload_to = __get_path_convo__,default= 'null')     
    upload_date = models.DateField()

    def __unicode__(self):
        return smart_unicode(self.title)

class CerdHome(models.Model):
    title = models.CharField(max_length = 100 )
    desription = models.TextField()
    Address = models.TextField()
    email  = models.EmailField()
    contact_no = models.IntegerField()

    def __unicode__(self):
        return smart_unicode(self.title)

class CerdPeople(models.Model):
    name = models.CharField(max_length= 100)
    dept = models.CharField(max_length= 100)
    desig = models.CharField(max_length= 100)
    profie_info = models.FileField(upload_to = __get_path_cerd__ ,default = 'null')    
    
    def __unicode__(self):
        return smart_unicode(self.name)
    
    
class RankList(models.Model):
    rank_id = models.IntegerField(primary_key = True)
    rank_name = models.CharField(max_length = 100, null = True, blank = True)

    def __unicode__(self):
        return smart_unicode(self.rank_name)

"""
class History(models.Model):
    rank_id = models.ForeignKey(RankList)
    name = models.CharField(max_length = 100, null = True, blank = True)
    tenure_start = models.CharField(max_length = 100, null = True, blank = True)
    tenure_end = models.CharField(max_length = 100, null = True, blank = True)
    photo = models.ImageField(upload_to = __get_path_directors__)

    def __unicode__(self):
        return smart_unicode(self.name)
"""
