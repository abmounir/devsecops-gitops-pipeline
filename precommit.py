import sys

# replcae the kubernetes image tag placeholder with a new image tag

with open("books.yaml", "r") as f:
    content = f.read()
with open("books.yaml", "w") as f:
    content = content.replace(sys.argv[1], 
                              sys.argv[2])
    f.write(content)
with open('argo-app.yaml', 'r') as f:
    content = f.read()
with open('argo-app.yaml', 'w') as f:
    content = content.replace(sys.argv[1], 
                              sys.argv[2])
    f.write(content)