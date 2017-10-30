from django.db import models

# Create your models here.

class Report(models.Model):
    """
    Model representing an investor user
    """
    report_name = models.CharField(max_length=500)
    company_name = models.CharField(max_length=100)
    CEO_name = models.CharField(max_length=100)
    company_phone = models.CharField(max_length=15)
    company_email = models.EmailField()
    company_location = models.CharField(max_length=200)
    company_country = models.CharField(max_length=50)
    sector = models.CharField(max_length=100)
    industry = models.CharField(max_length=100)
    current_project = models.CharField(max_length=80)
    private_report = models.BooleanField()
    files_attached = models.TextField()


    def __str__(self):
        """
        String for representing the Model object.
        """
        return '%s, %s' % (self.report_name, self.company_name, self.CEO_name, self.company_phone, self.company_email, self.company_location, self.company_country,
                           self.sector, self.industry, self.current_project, self.private_report, self.files_attached)

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.
        """
        return reverse('model-detail-view', args=[str(self.id)])

