from django.db import models

# Create your models here.

class Chart(models.Model):
    PIE = "PIE"
    H_BAR = "HBAR"
    V_BAR = "VBAR"
    LINE = "LINE"
    CHART_TYPE_CHOICE = [
        (PIE, "Pie Chart"),
        (H_BAR, "Horizontal Bar Chart"),
        (V_BAR, "Vertical Bar Chart"),
        (LINE, "Line Chart"),
    ]
    name = models.CharField("Chart Name", name="chart_name" , unique=True)
    chart_type = models.CharField("Type of Chart", name="chart_type", max_length=5, choices=CHART_TYPE_CHOICE, default=PIE)

class ChartDetail(models.Model):
    chart_id = models.ForeignKey("bar.Chart", on_delete=models.CASCADE)
    parm_name = models.CharField("Name of parameter", name="parm_name", max_length=50)
    parm_value = models.CharField("Value of the parameter", name="parm_value", max_length=2000)

class Data(models.Model):
    group1 = models.CharField("First Grouping", name="group1",max_length=100)
    group2 = models.CharField("Second Grouping", name="group2", max_length=100)
    element1 = models.IntegerField("First Element", name="element1")
    element2 = models.IntegerField("Second Element", name="element2")
    element3 = models.IntegerField("Third Element", name="element3")

    class Meta:
        indexes = [
            models.Index(fields=["group1","group2"], name="grps_idx"),
            models.Index(fields=["group1"], name="grp_1_idx")
        ]
        unique_together = [["group1", "group2"]]

