from django.db import models
from django.contrib.auth.models import User
from Pickup.models import PickUp
from Drop.models import Drop
from CustomerData.models import CustomerTrack
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Report(models.Model):
    #customer Track details
    STATUS=(('ASSIGNED','ASSIGNED'),('PENDING','PENDING'),('COMPLETED','COMPLETED'))
    customerName = models.CharField(max_length=255, null=True, blank=True)
    customer_address = models.TextField(max_length=255, null=True, blank=True)
    phNo = models.CharField(max_length=12, null=True, blank=True)
    email = models.EmailField(
        max_length=255, null=True, blank=True)
    rcNo = models.CharField(max_length=255, null=True, blank=True)
    purchase_date = models.DateTimeField(auto_now_add=True)
    model = models.CharField(max_length=255, null=True, blank=True)
    status=models.TextField(max_length=255, null=True, blank=True,choices=STATUS,default='COMPLETED')
    #pick details
    FUEL_CHOOSE = (
        ('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'),
    )

    OdoMeter = models.DecimalField(
        max_digits=5, decimal_places=0, null=True, blank=True)
    FuelLevel = models.CharField(
        max_length=7, default=('1', '1'), choices=FUEL_CHOOSE, null=True, blank=True)
    CDPlayer = models.BooleanField(default=False)
    CigeretteCharger = models.BooleanField(default=False)
    ToolKit = models.BooleanField(default=False)
    ServiceBook = models.BooleanField(default=False)
    Clock = models.BooleanField(default=False)
    CarPerfume = models.BooleanField(default=False)
    Jack = models.BooleanField(default=False)
    SpareWheel = models.BooleanField(default=False)
    Mats = models.BooleanField(default=False)
    DickyMat = models.BooleanField(default=False)
    BodyCover = models.BooleanField(default=False)
    Antenna = models.BooleanField(default=False)
    Remote = models.BooleanField(default=False)
    image1 = models.ImageField(
        null=True, blank=True, upload_to='photos/%Y/%m/%d/')
    image2 = models.ImageField(
        null=True, blank=True, upload_to='photos/%Y/%m/%d/')
    image3 = models.ImageField(
        null=True, blank=True, upload_to='photos/%Y/%m/%d/')
    image4 = models.ImageField(
        null=True, blank=True, upload_to='photos/%Y/%m/%d/')
    image5 = models.ImageField(
        null=True, blank=True, upload_to='photos/%Y/%m/%d/')
    customerRemarks = models.TextField(null=True, blank=False)
    # customerSignature = models.JSignatureField()
    pickup_User = models.ForeignKey(User,
                             on_delete=models.DO_NOTHING, null=True, blank=True,related_name='pickup_User')
    pick_date=models.CharField(max_length=255,null=True,blank=True)
    #drop details 
    customer_remarks = models.TextField(null=True, blank=True)
    drop_User = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, null=True, blank=True,related_name='drop_User')
    customer_token=models.CharField(null=True,blank=True,max_length=255)
    drop_date = models.CharField(max_length=255,null=True,blank=True)
   

# @receiver(post_save, sender=Drop)
# def SaveCompleteReport(sender, instance, **kwargs):
def SaveCompleteReport(instance,):
    customerTrackInstance=CustomerTrack.objects.get(customer_token=instance.customer_token)

    DropInstance=Drop.objects.get(customer_token=instance.customer_token)
    PickupInstance=PickUp.objects.get(customer_token=instance.customer_token)
    Report.objects.create(
        #customer details
        customerName=customerTrackInstance.name,
        customer_address=customerTrackInstance.address,
        phNo=customerTrackInstance.phNo,
        email=customerTrackInstance.email,
        rcNo=customerTrackInstance.rcNo,
        purchase_date=customerTrackInstance.purchase_date,
        status=customerTrackInstance.status,
        model=customerTrackInstance.model,
        

        #Pickup details
        OdoMeter=PickupInstance.OdoMeter,
        FuelLevel=PickupInstance.FuelLevel,
        CDPlayer=PickupInstance.CDPlayer,
        CigeretteCharger=PickupInstance.CigeretteCharger,
        ToolKit=PickupInstance.ToolKit,
        ServiceBook=PickupInstance.ServiceBook,
        Clock=PickupInstance.Clock,
        CarPerfume=PickupInstance.CarPerfume,
        Jack=PickupInstance.Jack,
        SpareWheel=PickupInstance.SpareWheel,
        Mats=PickupInstance.Mats,
        DickyMat=PickupInstance.DickyMat,
        BodyCover=PickupInstance.BodyCover,
        Antenna=PickupInstance.Antenna,
        Remote=PickupInstance.Remote,
        image1=PickupInstance.image1,
        image2=PickupInstance.image2,
        image3=PickupInstance.image3,
        image4=PickupInstance.image4,
        image5=PickupInstance.image5,
        pickup_User=PickupInstance.user,
        pick_date=PickupInstance.pick_date,

        #Drop Details
        customer_remarks=DropInstance.remarks,
        drop_User=DropInstance.user,
        drop_date=DropInstance.drop_date,
        customer_token=DropInstance.customer_token,
    )