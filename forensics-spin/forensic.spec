# Sabayon Linux 5 x86 GNOME Molecule remaster spec file
# The aim of this spec file is to add arbitrary applications & misc stuff
# to an already built ISO image via scripting (providing hooks that call
# user-defined scripts).
# squashfs, mkisofs needed

# Define an alternative execution strategy, in this case, the value must be
# "iso_remaster"
execution_strategy: iso_remaster

# Path to source ISO file (MANDATORY)
source_iso: /home/gru/iso/source/Sabayon_Linux_DAILY_amd64_GNOME-dev.iso

# Error script command, executed when something went wrong and molecule has to terminate the execution
# environment variables exported:
# - CHROOT_DIR: path to chroot directory, if any
# - CDROOT_DIR: path to livecd root directory, if any
# - SOURCE_CHROOT_DIR: path from where chroot is copied for final handling
# error_script: /path/to/script/to/be/executed/outside/after

# Outer chroot script command, to be executed outside destination chroot before
# before entering it (and before inner_chroot_script)
outer_chroot_script: /home/gru/spin/remaster_pre.sh

# Inner chroot script command, to be executed inside destination chroot before packing it
# - kmerge.sh - setup kernel bins
#  inner_chroot_script:

# Inner chroot script command, to be executed inside destination chroot after
# packages installation and removal
inner_chroot_script_after: /home/gru/spin/inner_chroot_script_after.sh

# Outer chroot script command, to be executed outside destination chroot before
# before entering it (and AFTER inner_chroot_script)
outer_chroot_script_after: /home/gru/spin/remaster_post.sh

# Extra mkisofs parameters, perhaps something to include/use your bootloader
extra_mkisofs_parameters: -b isolinux/isolinux.bin -c isolinux/boot.cat

# Pre-ISO building script. Hook to be able to copy kernel images in place, for example
pre_iso_script: /home/gru/Git/Coding/forensics-spin/pre_iso_script.sh

# Destination directory for the ISO image path (MANDATORY)
destination_iso_directory: /home/gru/iso/final

# Output iso image title
iso_title: Sabayon Forensics Spin

# Alternative ISO file mount command (default is: mount -o loop -t iso9660)
# iso_mounter:

# Alternative ISO umounter command (default is: umount)
# iso_umounter:

# Alternative squashfs file mount command (default is: mount -o loop -t squashfs)
# squash_mounter:

# Merge directory with destination LiveCD root
# merge_livecd_root: /put/more/files/onto/CD/root

# List of packages that would be removed from chrooted system (comma separated)
packages_to_remove:
        games-misc/cowsay,
        games-action/minetest_game,
		dev-python/wxpython,
		media-video/pitivi
		games-action/minetest,
		dev-python/wxpython

# Custom shell call to packages removal (default is: equo remove)
# custom_packages_remove_cmd:

# List of packages that would be added from chrooted system (comma separated)
packages_to_add:
        app-admin/testdisk,
        app-antivirus/clamav,
        app-antivirus/clamtk,
        app-forensics/magicrescue,
        app-forensics/cmospwd,
        app-forensics/rkhunter,
        app-forensics/sleuthkit,
        app-forensics/autopsy,
        app-forensics/mac-robber,
        app-forensics/memdump,
        app-forensics/aide,
        app-forensics/rifiuti-20040505_p1,
        app-forensics/unhide-20130526,
        app-crypt/chntpw,
        app-crypt/fcrackzip,
        app-crypt/johntheripper,
        app-crypt/gifshuffle,
        app-crypt/pdfcrack,
        app-crypt/WiRouterKeyRec,
        app-misc/calamares-sabayon,
        app-misc/screen,
        app-office/libreoffice,
        dev-util/geany,
        dev-util/geany-plugins,
        gnome-extra/nm-applet,
        gnome-extra/gnome-tweak-tool,
        dev-vcs/git,
        net-analyzer/ettercap,
        net-analyzer/traceroute,
        net-analyzer/w3af,
        net-libs/libnet,
        net-libs/netwib,
        net-misc/knock,
        net-vpn/tor,
        media-fonts/droid,
        media-gfx/pqstego,
        media-sound/pavucontrol,
        media-video/vlc,
        net-analyzer/nikto,
        net-analyzer/nmap,
        net-analyzer/netcat6,
        net-irc/irssi,
        net-ftp/filezilla,
        net-analyzer/wireshark,
        net-analyzer/tcpdump,
        net-misc/dropbox,
        net-proxy/torsocks,
        net-wireless/aircrack-ng,
        sys-apps/firejail,
        sys-apps/mlocate,
        sys-apps/gnome-disk-utility,
        sys-block/gparted,
        sys-boot/os-prober,
        sys-fs/extundelete,
        www-client/firefox,
        x11-libs/xcb-util-image,
        x11-libs/xcb-util-keysyms,
        x11-libs/xcb-util-wm,
        x11-terms/gnome-terminal,
        x11-themes/gtk-engines-murrine,
        x11-wm/awesome
        
# Custom shell call to packages add (default is: equo install)
# custom_packages_add_cmd:

# Custom command for updating repositories (default is: equo update)
# repositories_update_cmd:

# Determine whether repositories update should be run (if packages_to_add is set)
# (default is: no), values are: yes, no.
execute_repositories_update: yes

# Directories to remove completely (comma separated)
# paths_to_remove:

# Directories to empty (comma separated)
# paths_to_empty:
