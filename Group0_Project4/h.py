from flask import Flask, escape, request
import hashlib
import json

app = Flask(__name__)

@app.route('/')
def root():
    return "Hello, World!"

@app.route('/md5/<str_val>')
def md5_str(str_val):
    m = hashlib.md5()
    m.update(str_val.encode('utf8'))

    output = {
        "input": str_val,
        "output": m.hexdigest()
    }
    return json.dumps(output)


@app.route('/factorial/<int:num>')
def factorial(num):
    if num == 0:
        return 1
    else:
        return str(int(num *factorial(num-1)))
    
    output = {
        "input": num,
        "output": factorial(num)
    }
    return json.dumps(output)

@app.route('/fibonacci/<int:fib>')
def fibo(fib):
    nterms = int()    
    if fib<=1:
        return fib
    else:
        return fibo(fib-1)+fibo(fib-2)
    for i in range(nterms):
        fibo(i)  

    output = {
        "input": fib,
        "output": fibo
    }
    return json.dumps(output)

@app.route('/is-prime/<int:p>')
def prime(p):
    if (p==1):
        return False
    elif(p==2):
        return True
    else:
        for x in range (2,p):
            if(p % x==0):
                return False
        return True
    output = {
        "input": p,
        "output": prime(p)
    }
    return json.dumps(output)


if __name__=='__main__':
    app.run(host='0.0.0.0', port='5000')
