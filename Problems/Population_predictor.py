In a small town the population is p0 = 1000 at the beginning of a year. 
The population regularly increases by 2 percent per year and moreover 50 new inhabitants per year come to live in the town.
How many years does the town need to see its population greater or equal to p = 1200 inhabitants?

Simplify the problem : Build a Algorithm to predict the year in which the population reaches a certain threshold.
Input :  Current population, Percentage , Immigrants, Threshold population.
Output :  No . of years.

Code :


    def nb_year(p0, percent, aug, p):
      c = 0
      def recur(p0, percent, aug, p,c):

        p0 = p0 + (percent/100)*p0 + aug
        c += 1
        if(p0<p):
          return recur(p0, percent, aug, p,c)
        else:
          return c
      return recur(p0, percent, aug, p,c)
      
Sample Input : nb_year(1500, 5, 100, 5000) 
Output :  15
