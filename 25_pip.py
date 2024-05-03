# pip package

# If you do not have PIP installed, you can download and install it from this page: https://pypi.org/project/pip/ 

try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")
  
#   finally can be used to clean up the resources very important