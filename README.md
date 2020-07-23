# benefits_comparison

> **----------------------------------------------------------**  
> ***DISCLAIMER*** I have not validated any of this rigorously  
> in any way.  It's not meant to actually be used in decision  
> making, or so I have to say.  
> **----------------------------------------------------------**

An estimate of how much you'll pay each year based on plan and number of visits of certain types.

1. Run "run_comparison.py"
1. A graph should pop up.  By default it shows you the BASELINE amount you'll pay with NO medical bills.  Basically just the premiums.
1. on the bottom you'll see a bunch of input boxes.  These are pairs of "number of visits/price per visit".
  1. from left to right: Office visit, specialist visit, virtual visit, urgent care visit, ER visit, outpatient surgery, hospital stay
1. Modify the number of visits for a given box and press "enter" to update the graph.

NOTES:
- Costs are ESTIMATES I have no idea what these things cost.  Feel free to change them.
- Individual plans are aware of a copays.  So if you add 1 `office visit` that says it costs 300, the plans with an office visit copay ignore the 300 and add the copay.  the plans without a copay use that cost to calculate a percentage. 
- It's all just an estimate/crap shoot.
