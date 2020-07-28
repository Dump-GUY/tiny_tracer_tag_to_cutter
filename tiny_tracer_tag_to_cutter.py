#Option1: Drag and Drop .tag file produced by tiny_tracer.
#Option2: run script, example: tiny_tracer_tag_to_cutter.py Malware.exe.tag
#                     example: tiny_tracer_tag_to_cutter.py "C:\Users\XXX\Desktop\TAG_TO_CUTTER\Malware.exe.tag"
#Tag file will be converted to Cutter annotation script.
import sys, base64
try:
    droppedTagFile = sys.argv[1] 
    Tag_file = open(droppedTagFile,'r').read()
    Cutter_RVA = []
    Cutter_comment = []
    Cutter_script = ""
    for k in range (0,len(Tag_file.split("\n")) -1):
        if Tag_file.split("\n")[k][0] != '>':
            Cutter_RVA.append(Tag_file.split("\n")[k].split(';')[0])
            Cutter_comment.append(Tag_file.split("\n")[k].split(';')[1])
            Cutter_script += "CCu base64:" + base64.b64encode(Cutter_comment[k].encode("utf-8")).decode() + " @ " + "$B+0x" + Cutter_RVA[k] +"\n"
    f = open(droppedTagFile + '.cutter.r2', "w").write(Cutter_script)     

except IndexError:
    print("No file dropped....\nDrag and drop .tag file or see examples:\ntiny_tracer_tag_to_cutter.py Malware.exe.tag\ntiny_tracer_tag_to_cutter.py\"C:\\Users\\XXX\\Desktop\\TAG_TO_CUTTER\\Malware.exe.tag\"\n")




