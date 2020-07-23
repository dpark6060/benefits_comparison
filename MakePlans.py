import InsuranceClass as ic




##########################################

UHC500_costs= {
    'pc_cost':35,'pc_copay':True,
    'sv_cost':60,'sv_copay':True,
    'vv_cost': 20, 'vv_copay': True,
    'uc_cost':75,'uc_copay':True,
    'er_cost':250,'er_copay':True,
    'os_cost':.2,'os_copay':False,
    'hs_cost':.2,'hs_copay':False
}

UHC500 = ic.Plan(**UHC500_costs)
UHC500.premium = 102.4
UHC500.INdeductible = 500
UHC500.ONdedutable = 1000
UHC500.INmax = 5000
UHC500.ONmax = 10000
UHC500.name='UHC 500'




##########################################

UHC1000_costs= {
    'pc_cost':35,'pc_copay':True,
    'sv_cost':60,'sv_copay':True,
    'vv_cost':20,'vv_copay':True,
    'uc_cost':75,'uc_copay':True,
    'er_cost':250,'er_copay':True,
    'os_cost':.2,'os_copay':False,
    'hs_cost':.2,'hs_copay':False
}

UHC1000 = ic.Plan(**UHC1000_costs)
UHC1000.premium = 91.02
UHC1000.INdeductible = 1000
UHC1000.ONdedutable = 2000
UHC1000.INmax = 4500
UHC1000.ONmax = 9000
UHC1000.name='UHC 1000'





##########################################
UHC1500_costs= {
    'pc_cost':35,'pc_copay':True,
    'sv_cost':60,'sv_copay':True,
    'vv_cost':20,'vv_copay':True,
    'uc_cost':75,'uc_copay':True,
    'er_cost':250,'er_copay':True,
    'os_cost':.2,'os_copay':False,
    'hs_cost':.2,'hs_copay':False
}

UHC1500 = ic.Plan(**UHC1500_costs)
UHC1500.premium = 89.02
UHC1500.INdeductible = 1500
UHC1500.ONdedutable = 3000
UHC1500.INmax = 6350
UHC1500.ONmax = 12700
UHC1500.name='UHC 1500'



##########################################
UHC2500_costs= {
    'pc_cost':40,'pc_copay':True,
    'sv_cost':70,'sv_copay':True,
    'vv_cost': 20, 'vv_copay': True,
    'uc_cost':75,'uc_copay':True,
    'er_cost':250,'er_copay':True,
    'os_cost':.2,'os_copay':False,
    'hs_cost':.2,'hs_copay':False
}

UHC2500 = ic.Plan(**UHC2500_costs)
UHC2500.premium = 71.66
UHC2500.INdeductible = 2500
UHC2500.ONdedutable = 5000
UHC2500.INmax = 6850
UHC2500.ONmax = 13700
UHC2500.name='UHC 2500'


##########################################

UHC6000_costs= {
    'pc_cost':40,'pc_copay':True,
    'sv_cost':70,'sv_copay':True,
    'vv_cost': 20, 'vv_copay': True,
    'uc_cost':75,'uc_copay':True,
    'er_cost':500,'er_copay':True,
    'os_cost':.2,'os_copay':False,
    'hs_cost':.2,'hs_copay':False
}

UHC6000 = ic.Plan(**UHC6000_costs)
UHC6000.premium = 57.64
UHC6000.INdeductible = 6000
UHC6000.ONdedutable = 12000
UHC6000.INmax = 7000
UHC6000.ONmax = 14000
UHC6000.name='UHC 6000'

##########################################
HDHP1500_costs= {
    'pc_cost':.1,'pc_copay':False,
    'sv_cost':.1,'sv_copay':False,
    'vv_cost': .1, 'vv_copay': False,
    'uc_cost':.1,'uc_copay':False,
    'er_cost':.1,'er_copay':False,
    'os_cost':.1,'os_copay':False,
    'hs_cost':.1,'hs_copay':False
}

HDHP1500 = ic.Plan(**HDHP1500_costs)
HDHP1500.premium = 42.96
HDHP1500.INdeductible = 1500
HDHP1500.ONdedutable = 3000
HDHP1500.INmax = 4000
HDHP1500.ONmax = 8000
HDHP1500.name='HDHP 1500'
##########################################


HDHP3000_costs= {
    'pc_cost':.1,'pc_copay':False,
    'sv_cost':.1,'sv_copay':False,
    'vv_cost': .1, 'vv_copay': False,
    'uc_cost':.1,'uc_copay':False,
    'er_cost':.1,'er_copay':False,
    'os_cost':.1,'os_copay':False,
    'hs_cost':.1,'hs_copay':False
}

HDHP3000 = ic.Plan(**HDHP3000_costs)
HDHP3000.premium = 46.96
HDHP3000.INdeductible = 3000
HDHP3000.ONdedutable = 6000
HDHP3000.INmax = 6650
HDHP3000.ONmax = 13300
HDHP3000.name='HDHP 3000'


##########################################

HDHP5000_costs= {
    'pc_cost':.2,'pc_copay':False,
    'sv_cost':.2,'sv_copay':False,
    'vv_cost': .2, 'vv_copay': False,
    'uc_cost':.2,'uc_copay':False,
    'er_cost':.2,'er_copay':False,
    'os_cost':.2,'os_copay':False,
    'hs_cost':.2,'hs_copay':False
}

HDHP5000 = ic.Plan(**HDHP5000_costs)
HDHP5000.premium = 27.94
HDHP5000.INdeductible = 5000
HDHP5000.ONdedutable = 10000
HDHP5000.INmax = 6650
HDHP5000.ONmax = 13300
HDHP5000.name='HDHP 5000'














