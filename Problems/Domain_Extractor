Problem :  Extract domain name from input url.

Input : A string (Url)

Output :  String (Domain Name)

Example : I :https://github.com/CadmusFlux/  O: github
          I :agar.io  O: agar
          I :www.google.ru  O: google
          

Code : 
      
      def domain_name(url):
      
        if url[0]=="w" and url[1]=="w":
              for j in range(4,len(url)):
                        if url[j]==".":
                            return url[4:j]
        elif url[0] == "h":
            for i in range(len(url)):
                if url[i]=="/" and url[i+1]=="/":
                    if url[i+2]=="w" and url[i+3]=="w":
                        for j in range(i+6,len(url)):
                            if url[j]==".":
                                return url[i+6:j]
                    else:
                        for j in range(i+2,len(url)):
                            if url[j]==".":
                                return url[i+2:j]
        else :
            for i in range(len(url)):
                            if url[i]==".":
                                return url[:i]
