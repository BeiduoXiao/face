#coding:utf-8
import eye
import lip
import brow
import skin

def main(filepath):
    lip_similar=lip.lip(filepath)
    skin_similar=skin.skin(filepath)
    brow_similar=brow.brow(filepath)
    eye_similar=eye.eye(filepath)
    
    
    
    total_list=[0,0,0,0]
    
    lipcoe=0.40
    skincoe=0.40
    browcoe=0.15
    eyecoe=0.05
    
    #spring
    total_list[0]=lipcoe*lip_similar[0]+skincoe*skin_similar[0]+browcoe*brow_similar[0]+eyecoe*eye_similar[0]
    #summer
    total_list[1]=lipcoe*lip_similar[1]+skincoe*skin_similar[1]+browcoe*brow_similar[1]+eyecoe*eye_similar[1]
    #fall
    total_list[2]=lipcoe*lip_similar[2]+skincoe*skin_similar[2]+browcoe*brow_similar[2]+eyecoe*eye_similar[2]
    #winter
    total_list[3]=lipcoe*lip_similar[3]+skincoe*skin_similar[3]+browcoe*brow_similar[3]+eyecoe*eye_similar[3]
    
    print "嘴：%s"%(lip_similar)
    print "肤：%s"%(skin_similar)
    print "眉：%s"%(brow_similar)
    print "眼：%s"%(eye_similar)
    
    print total_list

if __name__ == '__main__':
    filepath='testcases/1111.jpeg'
    main(filepath)