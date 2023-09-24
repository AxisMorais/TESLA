import smtplib
import email.message


def enviarEmail():
    corpo_Email = """
      <p> Prezados, </p>

      <p> Para fins de teste, segue o teste do primeiro e-mail. </p>
      <p> Cordialmente </p>

      <p>Thiago C. Morais | Gerência de Custos - GCUST </p>   
      <p>Secretaria Municipal de Planejamento, Orçamento e Gestão - SMPOG </p>   
      <p> Avenida Augusto de Lima, 30 | 11° Andar | Centro | BH/MG </p>   
      <p> (31) 3246-0528 | (31) 97170-2836 www.pbh.gov.br </p>
    """

    msg = email.message.Message()
    # Título do e-mail
    msg['Subject'] = "E-mail automático TESTE"
    # Autor
    msg['From'] = 'thiago.conegundes@edu.pbh.gov.br'
    # Criando lista de Destinatários
    destinatarios = ['thiago.conegundes@gmail.com' , 'thiago.conegundes@edu.pbh.gov.br' ]

    password = 'Th1505@'
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_Email)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()

    # Login credentials for sending email
    s.login(msg['From'], password)

    # Concatenar os destinatários em uma única string
    msg['To'] = ", ".join(destinatarios)

    s.sendmail(msg['From'], destinatarios, msg.as_string().encode('utf-8'))
    print('Email enviado para todos os destinatários')

enviarEmail()