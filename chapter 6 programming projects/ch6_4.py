# harrison frahn
# period 2
# chapter 6.4
# expected input: the first term, common ratio, and number of terms
from graphics import *
def est_val(term1, common_ratio, num_terms):
    total = term1
    for i in range(num_terms-1):
        term1 *= common_ratio
        total += term1
    return total
def main():
	win = GraphWin("Convergence Calculator", 400, 200)
	Text(Point(200,20),"This program calculates the convergence of an infinte series.").draw(win)
	entry1 = Entry(Point(200,50),13); entry1.setText("First Term"); entry1.draw(win)
	entry2 = Entry(Point(200,100),13); entry2.setText("Common Ratio"); entry2.draw(win)
	entry3 = Entry(Point(200,150),13); entry3.setText("# of Terms"); entry3.draw(win)
	Text(Point(200,180),"Click to Calculate").draw(win)
	win.getMouse()
	term1, common_ratio, num_terms =eval(entry1.getText()),eval(entry2.getText()),eval(entry3.getText())
	win.close()
	win1 = GraphWin("Results", 200,200)
	est_value = est_val(term1,common_ratio,num_terms) 
	Text(Point(100,50),"Estimated value: "+str(est_value)).draw(win1)
	actual = term1 / (1-common_ratio)
	Text(Point(100,100),"Actual value: "+str(actual)).draw(win1)
	error = abs(est_value-actual)
	Text(Point(100,150),"Error: "+str(error)).draw(win1)
	Text(Point(100,175),"Click to quit:").draw(win1)
	win1.getMouse()
main()