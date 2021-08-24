Problem statement : Not a CP problem , but this is a function I needed for a certain program I am developing.
                    It is not a  coding challenge a per se just a interesting thing i encountered. Unix time is the time in seconds which calculates the seconds that has elapsed
                    from january 1 , 1970 . PRAW returns post time in Unix time . Hence this program. Thanks for coming to my TED talk. 
                    
            
Code : 
      
        def unix_year(time):
          month = ((time/86400)//365)
          year = 1970 + int(month)
          return year
          
P.S  : There's a lot of simplification in this code regarding alternating days in a month , floor division , also leap year and leap seconds (Utc time - atomic time difference)
