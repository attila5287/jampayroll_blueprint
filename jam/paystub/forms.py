from flask_wtf import FlaskForm
from wtforms import (
    StringField, IntegerField, DecimalField
)
from wtforms.validators import (
    DataRequired, Length, Email, EqualTo, ValidationError
)


class PayStubForm(FlaskForm):
    firstName = StringField('first name', validators=[
                            DataRequired()], default='Attila')
     
    middleName = StringField('middle name', default='')
    
    lastName = StringField('last name', validators=[
                           DataRequired()], default='Turkoz')
    
    companyName = StringField('company', validators=[
                              DataRequired()], default='JAM')
    
    allowance = IntegerField('allowance', default=2)
    
    hourlyRate = DecimalField('hourly rate', validators=[
                              DataRequired()], default=44.00)
    
    hoursWorked = DecimalField('hours worked', validators=[
                              DataRequired()], default=80.00)
    
    payCntYr2Dt = IntegerField('pay count YTD', default=2)
    
    dateStart =  StringField('mm/dd/yyyy', validators=[
                              DataRequired()], default='11/04/2019')
    
    dateEnd =  StringField('mm/dd/yyyy', validators=[
                              DataRequired()], default='11/17/2019')

    def generate_paystub(self, *args, **kwargs):
        super(ModGeneratedPayStubFrom, self).__init__(*args, **kwargs)
        self.payCntYr2Dt = payCntYr2Dt
        self.dateStart = dateStart
        self.dateEnd = dateEnd
        self.allowance_regression_slope = -0.1067
        self.allowance_regression_intcpt = 2.0444 
        self.allowanceFactor = float(self.allowance_regression_slope * self.allowance.data) +  self.allowance_regression_intcpt
        self.current = self.hoursWorked * self.hourlyRate
        self.curr3nt = self.hoursWorked * self.hourlyRate
        self.year2date = payCntYr2Dt * self.current
        self.hourlyR4te = self.hourlyRate
        self.year2d4te = self.year2date
        self.social_security = self.current * self.allowanceFactor *9.3/150
        self.social_security_perc = self.allowanceFactor *9.3/150*100
        self.social_security_year2date = self.current *  self.allowanceFactor *9.3 / 150 * payCntYr2Dt
        self.medicare = self.current *  self.allowanceFactor *2.18 / 150
        self.medicare_perc = self.allowanceFactor *2.18 / 150*100
        self.medicare_year2date = self.current * 2.18 / 150 *  self.allowanceFactor *payCntYr2Dt
        self.futa = self.current * 0.90 * self.allowanceFactor / 150
        self.futa_perc = 0.90 * self.allowanceFactor / 150*100
        self.futa_year2date = self.current * 0.90 / 150 *  self.allowanceFactor *payCntYr2Dt
        self.co_unemp = self.current * self.allowanceFactor * 1.77 / 150
        self.co_unemp_perc = self.allowanceFactor * 1.77 / 150*100
        self.co_unemp_year2date = self.current * 1.77 / 150 * payCntYr2Dt * self.allowanceFactor 
        self.taxes = self.current * 11.48 / 150 * self.allowanceFactor
        self.taxes_perc = 11.48 / 150 * self.allowanceFactor *100 
        self.taxes_year2date = self.current * 11.48 / 150 * payCntYr2Dt * self.allowanceFactor
        self.net_pay = self.current*(1-(11.48/150*self.allowanceFactor))
        self.net_pay_perc = (1-(11.48/150*self.allowanceFactor))*100
        self.net_pay_y2d =  self.current*(1-(11.48/150*self.allowanceFactor))* payCntYr2Dt

    def __rpr__(self):
        pass
        print('test PayStubForm')



