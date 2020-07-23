
class Plan:
    def __init__(self,pc_cost=35, pc_copay=True,
                      sv_cost=60, sv_copay=True,
                      vv_cost=20, vv_copay=True,
                      uc_cost=75, uc_copay=True,
                      er_cost=250, er_copay=True,
                      os_cost=.2, os_copay=False,
                      hs_cost=.2, hs_copay=False):
        self.INdeductible = 0
        self.ONdedutable = 0
        self.INmax = 0
        self.ONmax = 0
        self.premium = 0
        self.deductible_charges = 0
        self.copay_charges = 0
        self.name=''
        
        
        self.pc_cost = pc_cost
        self.pc_copay = pc_copay
        self.sv_cost = sv_cost
        self.sv_copay = sv_copay
        self.vv_cost = vv_cost
        self.vv_copay = vv_copay
        self.uc_cost = uc_cost
        self.uc_copay = uc_copay
        self.er_cost = er_cost
        self.er_copay = er_copay
        self.os_cost = os_cost
        self.os_copay = os_copay
        self.hs_cost = hs_cost
        self.hs_copay = hs_copay
        
    
    def add_INcharge(self, charge):
        
        if charge.copay:
            self.copay_charges += charge.amount
        
        else:
            
            # If we're over our deductible
            if self.deductible_charges > self.INdeductible:
                
                # If we're over our max
                if self.deductible_charges >= self.INmax:
                    # No new fee
                    new_amount = 0
                
                # Otherwise the fee is the charge * deductible modifier
                else:
                    new_amount = charge.amount*charge.amount_paid_after_deductible
                
            # If we're not yet at our deductible:
            else:
                
                #If this puts us over our deductible
                if charge.amount + self.deductible_charges > self.INdeductible:
                    
                    amount_to_deductible = self.INdeductible - self.deductible_charges
                    
                    new_amount = amount_to_deductible + (charge.amount - amount_to_deductible)*charge.amount_paid_after_deductible
                else:
                    new_amount = charge.amount 
            
            self.deductible_charges += new_amount
            
            if self.deductible_charges > self.INmax:
                self.deductible_charges = self.INmax
    
    
    def get_annual_cost(self):
        cost = self.copay_charges + self.premium*24 + self.deductible_charges
        return(cost)
    
    
    def primary_care(self, cost=0):
        charge = Charge()
        charge.copay = self.pc_copay
        if charge.copay:
            charge.adds_after_max = True
            charge.adds_to_deductible = False
            charge.amount_paid_before_deductible = 1
            charge.amount_paid_after_deductible = 1
            charge.amount = self.pc_cost
        else:
            charge.adds_after_max = True
            charge.adds_to_deductible = False
            charge.amount_paid_before_deductible = 1
            charge.amount_paid_after_deductible = self.pc_cost
            charge.amount = cost

        
        return(charge)

    def specialist_visit(self, cost=0):
        charge = Charge()
        charge.copay = self.sv_copay
        if charge.copay:
            charge.adds_after_max = True
            charge.adds_to_deductible = False
            charge.amount_paid_before_deductible = 1
            charge.amount_paid_after_deductible = 1
            charge.amount = self.sv_cost
        else:
            charge.adds_after_max = False
            charge.adds_to_deductible = True
            charge.amount_paid_before_deductible = 1
            charge.amount_paid_after_deductible = self.sv_cost
            charge.amount = cost

        return (charge)
    
    def virtual_visit(self, cost=0):
        charge = Charge()
        charge.copay = self.vv_copay
        if charge.copay:
            charge.adds_after_max = True
            charge.adds_to_deductible = False
            charge.amount_paid_before_deductible = 1
            charge.amount_paid_after_deductible = 1
            charge.amount = self.vv_cost
        else:
            charge.adds_after_max = False
            charge.adds_to_deductible = True
            charge.amount_paid_before_deductible = 1
            charge.amount_paid_after_deductible = self.vv_cost
            charge.amount = 0

        return (charge)
    
    def urgent_care(self,cost=0):
        charge = Charge()
        charge.copay = self.uc_copay
        if charge.copay:
            charge.adds_after_max = True
            charge.adds_to_deductible = False
            charge.amount_paid_before_deductible = 1
            charge.amount_paid_after_deductible = 1
            charge.amount = self.uc_cost
        else:
            charge.adds_after_max = False
            charge.adds_to_deductible = True
            charge.amount_paid_before_deductible = 1
            charge.amount_paid_after_deductible = self.uc_cost
            charge.amount = cost

        return (charge)
    
    def er_visit(self, cost=0):
        charge = Charge()
        charge.copay = self.er_copay
        if charge.copay:
            charge.adds_after_max = True
            charge.adds_to_deductible = False
            charge.amount_paid_before_deductible = 1
            charge.amount_paid_after_deductible = 1
            charge.amount = self.er_cost
        else:
            charge.adds_after_max = False
            charge.adds_to_deductible = True
            charge.amount_paid_before_deductible = 1
            charge.amount_paid_after_deductible = self.er_cost
            charge.amount = cost

        return (charge)
    
    def outpatient_surgery(self, cost=0):
        charge = Charge()
        charge.copay = self.os_copay
        if charge.copay:
            charge.adds_after_max = True
            charge.adds_to_deductible = False
            charge.amount_paid_before_deductible = 1
            charge.amount_paid_after_deductible = 1
            charge.amount = self.os_cost
        else:
            charge.adds_after_max = False
            charge.adds_to_deductible = True
            charge.amount_paid_before_deductible = 1
            charge.amount_paid_after_deductible = self.os_cost
            charge.amount = cost

        return (charge)
    
    def hospital_stay(self, cost=0):
        charge = Charge()
        charge.copay = self.hs_copay
        if charge.copay:
            charge.adds_after_max = True
            charge.adds_to_deductible = False
            charge.amount_paid_before_deductible = 1
            charge.amount_paid_after_deductible = 1
            charge.amount = self.hs_cost
        else:
            charge.adds_after_max = False
            charge.adds_to_deductible = True
            charge.amount_paid_before_deductible = 1
            charge.amount_paid_after_deductible = self.hs_cost
            charge.amount = cost
        return (charge)


class Charge:
    
    def __init__(self, amount=0):
        self.copay = True
        self.adds_to_deductible = False
        self.amount_paid_before_deductible = 1
        self.amount_paid_after_deductible = 1
        self.amount = amount
        self.adds_after_max = True
        
    
    