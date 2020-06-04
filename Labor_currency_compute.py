from num2words import num2words                                                 
                                                                                
def laborrencycompute(hourly,children,danger,skills,importance,demand,quality): 
    """This Function calculates wages in the Federation of Cooperatives.        
       There is a Minimum Base wage of $15 Laborrency Coins, and 5              
       Additional Variables which are all multipliers of the hourly Wage        
       This Laborrency seeks to be On Demand - Guaranteed - Living Wage -       
       Meritocratic. """                                                        
                                                                                
    var1_hourly = hourly+(hourly*(children*.5)) # Minimum $15.00                
    var2_danger = hourly*danger # Multiply by 3                                 
    var3_skills = hourly*skills # Multiply by 3                                 
    var4_importance = hourly*importance # Multiply by 6                         
    var5_demand = hourly*demand # Multiply by 2                                 
    var6_quality = hourly*quality # Multiply by 7                               
                                                                                
    tophourly = var1_hourly+var2_danger+var3_skills+var4_importance+\           
                var5_demand+var6_quality                                        
    topweekly = tophourly*40                                                    
    topmonthly = topweekly*4.33                                                 
    topyearly = topmonthly*12                                                   
                                                                                
    print(f"""{chr(10)}                                                         
              Hourly Pay is {num2words(tophourly)} Laborrency{chr(10)}          
              Weekly Pay is {num2words(topweekly)}{chr(10)}                     
              Monthly Pay is {num2words(topmonthly)}{chr(10)}                   
              Yearly Pay is {num2words(topyearly)}                              
              {chr(21328)}""") 
    
productivelabor = """There is one sort of labour which adds to the value of the subject upon which it is bestowed; 
there is another which has no such effect. The former, as it produces a value, may be called productive; the latter, 
unproductive labour. Thus the labour of a manufacturer adds, generally, to the value of the materials which he works upon, 
that of his own maintenance, and of his master's profit. The labour of a menial servant, on the contrary, adds to the value
of nothing. Though the manufacturer has his wages advanced to him by his master, he, in reality, costs him no expense, 
the value of those wages being generally restored, together with a profit, in the improved value of the subject upon which 
his labour is bestowed. But the maintenance of a menial servant never is restored. A man grows rich by employing a 
multitude of manufacturers; he grows poor by maintaining a multitude of menial servants. The labour of the latter, 
however, has its value, and deserves its reward as well
— Adam Smith, The Wealth of Nations"""
                                                                                
if __name__ == '__main__':                                                      
    laborrencycompute(15,4,0,0,0,0,0)  
