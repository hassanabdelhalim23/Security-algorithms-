#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, request, jsonify
from flask import render_template
from algos import security
from algos import caesar
from algos import polyAlphabetic
from algos import hill
from algos import rsa
from algos import one_time_pad as otp
from algos.DES import Data

app = Flask(__name__)


@app.route('/des', methods=['GET'])
def des():
    object = Data.DESdata('133457799BBCDFF1', '0123456789ABCDEF')

    # TO DO TASKS performs are operations Must be in order

    object.init_ip()
    object.intit_R0andL0()
    object.initkey()
    object.ROunds()

    # in this function returns data in bits

    data = object.final_ip()

    # in this function return Data In Hex Decimal

    return jsonify(output=object.finato(data))


    # after this if you would Like to display keys or R or  L
    # object.RofRounds  #displays R From R0 To R16
    # object.LofRounds  ##displays L From L0 To L16
    # object.Keysafterpermulation #Displays Keys
    # return object.RofRounds

@app.route('/', methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        text = ''

        # ##########################################################################################

        if request.form['contact-name'] == 'Caesar':
            if request.form['type'] == 'enc':
                try:
                    text = caesar.encrypt(request.form['text'],
                            int(request.form['key']))
                except:
                    return render_template('index.html',
                            error='Malformed entries.')
                return render_template('index.html', text=text,
                        type='enc')
            else:
                try:
                    text = caesar.decrypt(request.form['text'],
                            int(request.form['key']))
                except:
                    return render_template('index.html',
                            error='Malformed entries.')
                return render_template('index.html', text=text,
                        type='dec')
        elif request.form['contact-name'] == 'Transposition':

        # ##########################################################################################

            if request.form['type'] == 'enc':
                try:
                    text = security.transportaion(request.form['text'],
                            request.form['key'])
                except:
                    return render_template('index.html',
                            error='Malformed entries.')
                return render_template('index.html', text=text,
                        type='enc')
            else:
                try:
                    print (request.form['text'], request.form['key'])
                    text = \
                        security.transportation_rev(request.form['text'
                            ], request.form['key'])
                    print (text)
                except:
                    return render_template('index.html', text=text,
                            error='Malformed entries.')
                return render_template('index.html', text=text,
                        type='dec')
        elif request.form['contact-name'] == 'Play_Fair':

        # ##########################################################################################

            if request.form['type'] == 'enc':
                try:
                    text = security.playfair(request.form['text'],
                            request.form['key'])
                except:
                    return render_template('index.html',
                            error='Malformed entries.')
                return render_template('index.html', text=text,
                        type='enc')
            else:
                try:
                    text = security.playfair_rev(request.form['text'],
                            request.form['key'])
                except:
                    return render_template('index.html',
                            error='Malformed entries.')
                return render_template('index.html', text=text,
                        type='dec')
        elif request.form['contact-name'] == 'Poly_Alphabetic':

        # ##########################################################################################

            if request.form['type'] == 'enc':
                try:
                    text = polyAlphabetic.encrypt(request.form['text'],
                            request.form['key'])
                except:
                    return render_template('index.html',
                            error='Malformed entries.')
                return render_template('index.html', text=text,
                        type='enc')
            else:
                try:
                    text = polyAlphabetic.decrypt(request.form['text'],
                            request.form['key'])
                except:
                    return render_template('index.html',
                            error='Malformed entries.')
                return render_template('index.html', text=text,
                        type='dec')
        elif request.form['contact-name'] == 'Full_Vigenere':

        # ##########################################################################################

            if request.form['type'] == 'enc':
                try:
                    text = security.Full_vigener(request.form['text'],
                            request.form['key'])
                except:
                    return render_template('index.html',
                            error='Malformed entries.')
                return render_template('index.html', text=text,
                        type='enc')
            else:
                try:
                    text = security.Full_vigener_rev(request.form['text'
                            ], request.form['key'])
                except:
                    return render_template('index.html',
                            error='Malformed entries.')
                return render_template('index.html', text=text,
                        type='dec')
        elif request.form['contact-name'] == 'Affine':

        # ##########################################################################################

            if request.form['type'] == 'enc':
                try:
                    text = security.affine(request.form['text'],
                            int(request.form['df']),
                            int(request.form['key']))
                except:
                    return render_template('index.html',
                            error='Malformed entries.')
                return render_template('index.html', text=text,
                        type='enc')
            else:
                try:
                    text = security.affine_rev(request.form['text'],
                            int(request.form['df']),
                            int(request.form['key']))
                except:
                    return render_template('index.html',
                            error='Malformed entries.')
                return render_template('index.html', text=text,
                        type='dec')
        elif request.form['contact-name'] == 'Hill':

        # ##########################################################################################

            if request.form['type'] == 'enc':
                try:
                    text = hill.enc(request.form['text'],
                                    request.form['key'],
                                    int(request.form['key_dimensions']))
                except:
                    return render_template('index.html',
                            error='Malformed entries.')
                return render_template('index.html', text=text,
                        type='enc')
            else:
                try:
                    text = hill.dec(request.form['text'],
                                    request.form['key'],
                                    int(request.form['key_dimensions']))
                except:
                    return render_template('index.html',
                            error='Malformed entries.')
                return render_template('index.html', text=text,
                        type='dec')
        elif request.form['contact-name'] == 'Sub_Trans':

        # ##########################################################################################

            if request.form['type'] == 'enc':
                try:
                    text = \
                        security.comandofSubandtrans(request.form['text'
                            ])
                except:
                    return render_template('index.html',
                            error='Malformed entries.')
                return render_template('index.html', text=text,
                        type='enc')
            else:
                try:
                    text = \
                        security.comandofSubandtrans_rev(request.form['text'
                            ])
                except:
                    return render_template('index.html',
                            error='Malformed entries.')
                return render_template('index.html', text=text,
                        type='dec')
        elif request.form['contact-name'] == 'One_Time_Pad':

        # ##########################################################################################

            if request.form['type'] == 'enc':
                try:
                    text = otp.one_time_pad(request.form['text'],
                            request.form['key'], 'enc')
                except:
                    return render_template('index.html',
                            error='Malformed entries.')
                return render_template('index.html', text=text,
                        type='enc')
            else:
                try:
                    text = otp.one_time_pad(request.form['text'],
                            request.form['key'], 'dec')
                except:
                    return render_template('index.html',
                            error='Malformed entries.')
                return render_template('index.html', text=text,
                        type='dec')
        elif request.form['contact-name'] == 'RSA':

        # ##########################################################################################

            if request.form['type'] == 'enc':
                try:
                    print (int(request.form['p']), int(request.form['q'
                           ]), request.form['text'])
                    text = rsa.encrypt(int(request.form['p']),
                            int(request.form['q']), request.form['text'
                            ])
                    print (text)
                except:
                    return render_template('index.html',
                            error='Malformed entries.')
                return render_template('index.html', text=text,
                        type='enc')
            else:
                try:
                    text = rsa.decrypt(int(request.form['p']),
                            int(request.form['q']), request.form['text'
                            ])
                except:
                    return render_template('index.html',
                            error='Malformed entries.')
                return render_template('index.html', text=text,
                        type='dec')
        elif request.form['contact-name'] == 'DES':

        # ##########################################################################################

            try:
                object = Data.DESdata(request.form['text'],
                        request.form['key'])
                object.init_ip()
                object.intit_R0andL0()
                object.initkey()
                object.ROunds()
                data = object.final_ip()
                text = object.finato(data)
            except:
                return render_template('index.html',
                        error='Malformed entries.')
            return render_template('index.html', text=text, type='enc')
    return render_template('index.html')

if __name__ == '__main__':
    app.debug = True
    app.run()

