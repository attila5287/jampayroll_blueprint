from flask import render_template, url_for, flash, redirect, request, Blueprint
from jam.paystub.forms import PayStubForm
from jam.paystub.paystub import PayStub

paystub = Blueprint('paystub', __name__)

@paystub.route("/paystub/create", methods=["GET", "POST"])
def create_paystub():
    PayStubF0rm = PayStubForm()


    if request.method == "POST":
        pass
        generated_paystub = PayStub(
            firstName=request.form["firstName"],
            middleName=request.form["middleName"],
            lastName=request.form["lastName"],
            companyName=request.form["companyName"],
            allowance=int(request.form["allowance"]),
            hourlyRate=float(request.form["hourlyRate"]),
            hoursWorked=float(request.form["hoursWorked"]),
            payCntYr2Dt=int(request.form["payCntYr2Dt"]),
            dateStart=request.form["dateStart"], 
            dateEnd=request.form["dateEnd"]
        )
        
        return render_template(
            "created_paystub.html",
            Pay_stub=generated_paystub,
            title='Paystub Printable'
        )
        
    return render_template(
        "create_paystub.html",
        form=PayStubF0rm,
        title='Paystub Form'
    )
