import MakePlans as mp
import matplotlib.pyplot as pl
import numpy as np
from matplotlib.widgets import TextBox

def clear(insurance_list):
    
    for i in insurance:
        i.deductible_charges = 0
        i.copay_charges = 0
    
    return(insurance)

       





def calc_cost(insurance,office_visits,specialist_visit,
              virtual_visit,urgent_care,emergency_room,
              outpatient_surgery,hospital_visit,ov_price,
              sv_price,vv_price,uc_price,er_price,os_price,hv_price):

    insurance = clear(insurance)
    
    for i in insurance:
        
        price = ov_price
        for v in range(office_visits):
            charge = i.primary_care(price)
            i.add_INcharge(charge)
            
        price = sv_price
        for v in range(specialist_visit):
            charge = i.specialist_visit(price)
            i.add_INcharge(charge)
    
        price = vv_price
        for v in range(virtual_visit):
            charge = i.virtual_visit(price)
            i.add_INcharge(charge)
            
        price = uc_price
        for v in range(urgent_care):
            charge = i.urgent_care(price)
            i.add_INcharge(charge)
    
        price = er_price
        for v in range(emergency_room):
            charge = i.er_visit(price)
            i.add_INcharge(charge)
    
        price = os_price
        for v in range(outpatient_surgery):
            charge = i.outpatient_surgery(price)
            i.add_INcharge(charge)
    
        price = hv_price
        for v in range(hospital_visit):
            charge = i.hospital_stay(price)
            i.add_INcharge(charge)
    
    return(insurance)


def calc_with_global():
    global insurance
    insurance = calc_cost(insurance, office_visits, specialist_visit,
                          virtual_visit, urgent_care, emergency_room,
                          outpatient_surgery, hospital_visit, ov_price,
                          sv_price, vv_price, uc_price, er_price, os_price, hv_price)

    return(insurance)




u500=mp.UHC500
u1000=mp.UHC1000
u1500=mp.UHC1500
u2500=mp.UHC2500
u6000=mp.UHC6000
h1500=mp.HDHP1500
h3000=mp.HDHP3000
h5000=mp.HDHP5000

office_visits = 0
specialist_visit = 0
virtual_visit = 0
urgent_care = 0
emergency_room = 0
outpatient_surgery = 0
hospital_visit = 0

ov_price = 300
sv_price = 300
vv_price = 300
uc_price = 600
er_price = 2000
os_price = 6000
hv_price = 15000

insurance = [u500,u1000,u1500,u2500,u6000,h1500,h3000,h5000]




x = np.arange(len(insurance))
data = [i.get_annual_cost() for i in insurance]
labels = [i.name for i in insurance]


fig, ax = pl.subplots(figsize=(14,8))
l,=pl.plot(x,data)
pl.xticks(x,labels)



def nhv_action(text):
    global hospital_visit
    hospital_visit = int(text)
    insurance = calc_with_global()
    data = [i.get_annual_cost() for i in insurance]
    l.set_ydata(data)
    ax.set_ylim(np.min(data), np.max(data))
    pl.draw()
    print(data)

def npv_action(text):
    global office_visits
    office_visits = int(text)
    insurance = calc_with_global()
    data = [i.get_annual_cost() for i in insurance]
    l.set_ydata(data)
    ax.set_ylim(np.min(data), np.max(data))
    pl.draw()
    
def nsv_action(text):
    global specialist_visit
    specialist_visit = int(text)
    insurance = calc_with_global()
    data = [i.get_annual_cost() for i in insurance]
    l.set_ydata(data)
    ax.set_ylim(np.min(data), np.max(data))
    pl.draw()
    
def nvv_action(text):
    global virtual_visit
    virtual_visit = int(text)
    insurance = calc_with_global()
    data = [i.get_annual_cost() for i in insurance]
    l.set_ydata(data)
    ax.set_ylim(np.min(data), np.max(data))
    pl.draw()
    
def nucv_action(text):
    global urgent_care
    urgent_care = int(text)
    insurance = calc_with_global()
    data = [i.get_annual_cost() for i in insurance]
    l.set_ydata(data)
    ax.set_ylim(np.min(data), np.max(data))
    pl.draw()
    
def nerv_action(text):
    global emergency_room
    emergency_room = int(text)
    insurance = calc_with_global()
    data = [i.get_annual_cost() for i in insurance]
    l.set_ydata(data)
    ax.set_ylim(np.min(data), np.max(data))
    pl.draw()
    
def nosv_action(text):
    global outpatient_surgery
    outpatient_surgery = int(text)
    insurance = calc_with_global()
    data = [i.get_annual_cost() for i in insurance]
    l.set_ydata(data)
    ax.set_ylim(np.min(data), np.max(data))
    pl.draw()
    
###############################
def chv_action(text):
    global hv_price
    hv_price = float(text)
    insurance = calc_with_global()
    data = [i.get_annual_cost() for i in insurance]
    l.set_ydata(data)
    ax.set_ylim(np.min(data), np.max(data))
    pl.draw()

def cpv_action(text):
    global ov_price
    ov_price = float(text)
    insurance = calc_with_global()
    data = [i.get_annual_cost() for i in insurance]
    l.set_ydata(data)
    ax.set_ylim(np.min(data), np.max(data))
    pl.draw()
    
def csv_action(text):
    global sv_price
    sv_price = float(text)
    insurance = calc_with_global()
    data = [i.get_annual_cost() for i in insurance]
    l.set_ydata(data)
    ax.set_ylim(np.min(data), np.max(data))
    pl.draw()
    
def cvv_action(text):
    global vv_price
    vv_price = float(text)
    insurance = calc_with_global()
    data = [i.get_annual_cost() for i in insurance]
    l.set_ydata(data)
    ax.set_ylim(np.min(data), np.max(data))
    pl.draw()
    
def cucv_action(text):
    global uc_price
    uc_price = float(text)
    insurance = calc_with_global()
    data = [i.get_annual_cost() for i in insurance]
    l.set_ydata(data)
    ax.set_ylim(np.min(data), np.max(data))
    pl.draw()
    
def cerv_action(text):
    global er_price
    er_price = float(text)
    insurance = calc_with_global()
    data = [i.get_annual_cost() for i in insurance]
    l.set_ydata(data)
    ax.set_ylim(np.min(data), np.max(data))
    pl.draw()
    
def cosv_action(text):
    global os_price
    os_price = float(text)
    insurance = calc_with_global()
    data = [i.get_annual_cost() for i in insurance]
    l.set_ydata(data)
    ax.set_ylim(np.min(data), np.max(data))
    pl.draw()

############################


















npcv_box = pl.axes([0.05, 0.05, 0.05, 0.02])
npcv = TextBox(npcv_box, '#Office visits', initial='0')
npcv.on_submit(npv_action)

nscv_box = pl.axes([0.19, 0.05, 0.05, 0.02])
nscv = TextBox(nscv_box, '#Specialist visit', initial='0')
nscv.on_submit(nsv_action)

nvcv_box = pl.axes([0.33, 0.05, 0.05, 0.02])
nvcv = TextBox(nvcv_box, '#Virtual', initial='0')
nvcv.on_submit(nvv_action)

nucv_box = pl.axes([0.475,0.05, 0.05, 0.02])
nucv = TextBox(nucv_box, '#urgent care', initial='0')
nucv.on_submit(nucv_action)

nerv_box = pl.axes([0.61,0.05, 0.05, 0.02])
nerv = TextBox(nerv_box, '#ER visits', initial='0')
nerv.on_submit(nerv_action)

nosv_box = pl.axes([0.758,0.05, 0.05, 0.02])
nosv = TextBox(nosv_box, '#outpatient surg', initial='0')
nosv.on_submit(nosv_action)

nihv_box = pl.axes([0.9,0.05, 0.05, 0.02])
nihv = TextBox(nihv_box, '#hospital stay', initial='0')
nihv.on_submit(nhv_action)

################################################

pcc_box = pl.axes([0.05, 0.03, 0.05, 0.02])
pcc = TextBox(pcc_box, 'office $', initial=str(ov_price))
pcc.on_submit(cpv_action)

scc_box = pl.axes([0.19, 0.03, 0.05, 0.02])
scc = TextBox(scc_box, 'specialist $', initial=str(sv_price))
scc.on_submit(csv_action)

vcc_box = pl.axes([0.33, 0.03, 0.05, 0.02])
vcc = TextBox(vcc_box, 'vitrual $', initial=str(vv_price))
vcc.on_submit(cvv_action)

ucc_box = pl.axes([0.475,0.03, 0.05, 0.02])
ucc = TextBox(ucc_box, 'urgent care $', initial=str(uc_price))
ucc.on_submit(cucv_action)

erc_box = pl.axes([0.616,0.03, 0.05, 0.02])
erc = TextBox(erc_box, 'ER $', initial=str(er_price))
erc.on_submit(cerv_action)

osc_box = pl.axes([0.758,0.03, 0.05, 0.02])
osc = TextBox(osc_box, 'outpatient surg $', initial=str(os_price))
osc.on_submit(cosv_action)

ihc_box = pl.axes([0.9,0.03, 0.05, 0.02])
ihc = TextBox(ihc_box, 'Hospital $', initial=str(hv_price))
ihc.on_submit(chv_action)




pl.show()

    
    


