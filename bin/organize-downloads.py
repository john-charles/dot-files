#!/usr/bin/env python

import os, sys, time, subprocess
from os.path import expanduser, join, exists

def debug(*args):
    if '--debug' in sys.argv:
        print args

##FILE_LIST_DIRECTORY = 0x0001
class File:

    def __init__( self, file="." ):
        self.file = os.path.abspath( file )

    def getAbsoluteFile( self ):

        return self.file

    def getName( self ):

        return os.path.basename( self.file )

def getDir( *args ):
    path = join( *args )
    if not os.path.exists( path ):
        os.makedirs( path )
    lock = join( path, ".dontdelete" )
    if not os.path.exists( lock ):
        open( lock, "w" ).close()    
    return path


def getHome( REALHOME ):

    if exists( join( REALHOME, ".download_organizer.ini" ) ):
        from ConfigParser import SafeConfigParser

        config = SafeConfigParser()
        config.read( join( REALHOME, ".download_organizer.ini" ) )

        if config.has_option("General","PersonalFolder" ):
            HOME = config.get("General","PersonalFolder")
            print repr( HOME )
            
            if exists( HOME ):
                return HOME
    return REALHOME
        

    

HOME = getHome( expanduser('~') )


            

DOWNLOADS = getDir( HOME, "Downloads" )
INSTALLERS = getDir( HOME, 'Downloads', "Installers" )
WININST = getDir( INSTALLERS, "Windows" )
DEBINST = getDir( INSTALLERS, "Debian and Ubuntu" )
MACINST = getDir( INSTALLERS, "Mac OSX" )
ARCHIVES = getDir( HOME, 'Downloads', "Archives" )
DOCUMENTS = getDir( HOME, "Documents", "Downloaded" )
VIDEOS = getDir( HOME, 'Videos', "Downloaded" )
PICTURES = getDir( HOME, 'Pictures', time.strftime('%Y'), "Downloaded" )
TORRENTS = getDir( HOME, "Downloads", "Download Meta Files" )
IMAGES = getDir( HOME, "Downloads","Images" )
EXTRACTED = getDir( HOME, "Downloads", "Extracted" )
CODE_SNIPPETS = getDir( HOME, "Projects", "0_Snippets")
JARS_DIR = getDir( HOME, "Projects", "0_Libraries", "java", "jars" )

debug("SETUP DIRS")
    
def moveFile( src, dst ):

    def moveFile32( src, dst ):
    
        from win32com.shell import shell, shellcon
    
        shell.SHFileOperation (
            (0, shellcon.FO_MOVE, src, dst,
             shellcon.FOF_CONFIRMMOUSE,
             None, None)
        )

    import sys

    if sys.platform == 'win32':
        moveFile32( src, dst )

    if sys.platform == 'linux2':
        print "renaming %s to %s" % ( src, dst )
        if os.path.exists( dst ):
            name = os.path.basename( dst )
            dnam = os.path.dirname( dst )
            itr = 0

            while os.path.exists( dst ):
                itr = itr + 1
                dst = join( dnam, "(%i) %s" % ( itr, name ))

        try:
            os.rename( src, dst )
        except:
            os.system('mv "%s" "%s"' % ( src, dst ) )
        

            
def trash( path ):

    def trash32( path ):
        
        from win32com.shell import shell, shellcon
    
        shell.SHFileOperation (
            (0, shellcon.FO_DELETE, path, None,
             shellcon.FOF_CONFIRMMOUSE | shellcon.FOF_ALLOWUNDO,
             None, None)
        )

    trash32( path )

def sortFile( path ):
    
    name = File( path ).getName().lower()
    if name.endswith(".exe") or name.endswith(".msi"):
        moveFile( path, join( WININST, name ) )

    if name.endswith(".dmg"):
        moveFile( path, join( MACINST, name ) )

    if name.endswith(".deb"):
        moveFile( path, join( DEBINST, name ) )

    if name.endswith(".zip") or \
       name.endswith(".rar") or name.endswith(".gz" ) or \
       name.endswith(".bz2") or name.endswith(".tar") or \
       name.endswith(".7z")  or name.endswith(".tgz"):
        
        archive_file = getDir( ARCHIVES, name )
        moveFile( path, join( archive_file, name ) )

    if name.endswith(".jar"):

        moveFile( path, join( JARS_DIR, name ) )

    if name.endswith(".doc") or name.endswith(".docx") or \
       name.endswith(".odt") or name.endswith(".pdf")  or \
       name.endswith(".wps"):

        moveFile( path, join( DOCUMENTS, name ) )

    if name.endswith(".3gp") or name.endswith(".3g2") or \
       name.endswith(".asf") or name.endswith(".wmv") or \
       name.endswith(".avi") or name.endswith(".flv") or \
       name.endswith(".f4v") or name.endswith(".f4p") or \
       name.endswith(".f4a") or name.endswith(".f4b") or \
       name.endswith(".mpg") or name.endswith(".mpeg") or \
       name.endswith(".mp1") or name.endswith(".mp2") or \
       name.endswith(".mpv") or name.endswith(".mov") or \
       name.endswith(".mp4") or name.endswith(".m4v") or \
       name.endswith(".mkv") or name.endswith(".rm"):

        moveFile( path, join( VIDEOS, name ) )

    if name.endswith(".jpg") or name.endswith(".jpeg") or \
       name.endswith(".png") or name.endswith(".gif")  or \
       name.endswith(".xcf") or name.endswith(".psd")  or \
       name.endswith(".svg"):

        moveFile( path, join( PICTURES, name.capitalize() ) )

    if name.endswith(".torrent") or name.endswith(".miro"):

        moveFile( path, join( TORRENTS, name.capitalize() ) )

    if name.endswith(".iso") or name.endswith(".img") or \
       name.endswith(".vdi") or name.endswith(".wim"):

        moveFile( path, join( IMAGES, name.capitalize() ) )

    if name.endswith(".py")   or name.endswith(".pyw") or \
       name.endswith(".cc")   or name.endswith(".cpp") or \
       name.endswith(".h")    or name.endswith(".hpp") or \
       name.endswith(".bat")  or name.endswith(".sh")  or \
       name.endswith(".java") or name.endswith(".pl")  or \
       name.endswith(".php") or name.endswith(".css") or \
       name.endswith(".js")  or name.endswith(".html"):
        
        moveFile( path, join( CODE_SNIPPETS, name.capitalize() ) )

    if name.endswith('~'):

        trash( path )

        
def sortDir( dir ):

    for file in os.listdir( dir ):
        path = join( dir, file )
        if os.path.isdir( path ):
            sortDir( path )
    if os.listdir( dir ) == []:
        os.rmdir( dir )

def sortExtracted( dl ):

    for file in os.listdir( dl ):
        path = join( dl, file )
        if not os.path.exists( join( path, ".dontdelete") ):
            if os.path.isdir( path ):
                moveFile( path, join( EXTRACTED, file ) )

    

def main():
    
    dl = join( HOME, "Downloads" )
    for file in os.listdir( dl ):
        path = join( dl, file )
        if not os.path.isdir( path ):
            sortFile( path )
        elif file not in ['Archives','Extracted','Images','Installers']:
            sortDir( path )

    sortExtracted( dl )
    if sys.platform.startswith("win"):
        os.startfile(DOWNLOADS)
    else:
        os.system("nohup dolphin %s > /dev/null &" % DOWNLOADS )



if __name__ == '__main__':

    main()

    
    
    
