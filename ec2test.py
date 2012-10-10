import smtplib
import base64

from boto import ec2
from email.mime.text import MIMEText


needtostop = []
evanservers = []
essieservers = []
chrisservers = []
lanreservers = []
jeremyservers = []
davisservers = []
lyttleservers = []
camservers = []
neilservers = []
jonservers = []

emails = {
    "eweiss": "eweiss@yammer-inc.com",
    "jeremy": "jchamilliard@yammer-inc.com",
    "jroach": "jroach@yammer-inc.com",
    "cou": "cou@yammer-inc.com",
    "essie": "ehamadani@yammer-inc.com",
    "lowolabi": "lowolabi@yammer-inc.com",
    "davis": "bdavis@yammer-inc.com",
    "blyttle": "blyttle@yammer-inc.com",
    "neil": "nmccarthy@yammer-inc.com",
    "cmcgrane": "cmcgrane@yammer-inc.com"

}

servers = {
    "eweiss": evanservers,
    "jeremy": jeremyservers,
    "jroach": jonservers,
    "cou": chrisservers,
    "essie": essieservers,
    "lowolabi": lanreservers,
    "davis": davisservers,
    "blyttle": lyttleservers,
    "neil": neilservers,
    "cmcgrane": camservers
}

regions = ec2.regions()

for region in regions:
    #print region.name

    conn = ec2.connect_to_region(region.name)
    instances = conn.get_all_instances()

    if len(instances) > 0:
        for i in instances:
            current = i.instances[0]
            # print current.id
            keyname = current.key_name
            # print "Key name is " + keyname
            if ((keyname is not None) and (current.state == 'running') and (current.virtualization_type != "paravirtual")):
                keylower = keyname.lower()

                if keylower.startswith('essie'):
                    essieservers.append(current.tags["Name"])
                    if("essie" not in needtostop):
                        needtostop.append("essie")
                elif keylower.startswith('blyttle'):
                    lyttleservers.append(current.tags["Name"])
                    if("blyttle" not in needtostop):
                        needtostop.append("blyttle")
                elif keylower.startswith('cmcgrane'):
                    camservers.append(current.tags["Name"])
                    if("cmcgrane" not in needtostop):
                        needtostop.append("cmcgrane")
                elif keylower.startswith('cou'):
                    chrisservers.append(current.tags["Name"])
                    if("cou" not in needtostop):
                        needtostop.append("cou")
                elif keylower.startswith('lowolabi'):
                    lanreservers.append(current.tags["Name"])
                    if("lowolabi" not in needtostop):
                        needtostop.append("lowolabi")
                elif keylower.startswith('jroach'):
                    jonservers.append(current.tags["Name"])
                    if("jroach" not in needtostop):
                        needtostop.append("jroach")
                elif keylower.startswith('neil'):
                    neilservers.append(current.tags["Name"])
                    if("neil" not in needtostop):
                        needtostop.append("neil")
                elif keylower.startswith('eweiss'):
                    evanservers.append(current.tags["Name"])
                    if("eweiss" not in needtostop):
                        needtostop.append("eweiss")
                elif keylower.startswith('jeremy'):
                    jeremyservers.append(current.tags["Name"])
                    if("jeremy" not in needtostop):
                        needtostop.append("jeremy")

            # if current.virtualization_type != "paravirtual":

sender = 'eweiss@yammer-inc.com'

for rec in needtostop:
    receivers = emails[rec]
    reclist = servers[rec]

    msg = """From: AWS BitchSlap <eweiss@yammer-inc.com>
    Subject: [FINAL TEST] You still have AWS servers running...

    """

    msg = msg + "The following servers are still running: \n"

    for svr in reclist:
        msg = msg + "\n" + svr


    mylogin = "eweiss@yammer-inc.com"
    mypass = base64.b64decode("V2luZG93ODY=")

    smtpObj = smtplib.SMTP('smtp.gmail.com','587')
    smtpObj.starttls()
    smtpObj.login(mylogin,mypass)

    # print receivers
    # print msg
    smtpObj.sendmail(sender,receivers,msg)
    print "Sent email to " + receivers

#msg = recipient + " - Please shut down the following servers" + serverlist
