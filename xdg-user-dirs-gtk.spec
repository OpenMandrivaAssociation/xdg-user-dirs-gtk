%define name xdg-user-dirs-gtk
%define version 0.7
%define release %mkrel 1

Summary: XDG user dirs support for GNOME/GTK+
Name: %{name}
Version: %{version}
Release: %{release}
Source0: ftp://ftp.gnome.org/pub/GNOME/sources/xdg-user-dirs-gtk/%{name}-%{version}.tar.bz2
# (fc) 0.5-2mdv add KDE info to desktop file
Patch0: xdg-user-dirs-gtk-0.7-kde.patch
# (fc) 0.5-2mdv detect mdk-folders entries in gtk bookmarks and replace them with standard entries
Patch1: xdg-user-dirs-gtk-0.5-mdkfolders.patch
License: GPL
Group: Graphical desktop/GNOME
Url: http://www.gnome.org/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: gtk2-devel
BuildRequires: xdg-user-dirs
BuildRequires: perl-XML-Parser
Requires: xdg-user-dirs


%description
xdg-user-dirs-gtk is a companion to xdg-user-dirs that integrates it into
the Gnome desktop and Gtk+ applications.

It gets run during login and does two things:
* Tracks changes of locale and prompts the user so the directories
  can be changed.
* Creates a default gtk bookmarks file if there is none, based
  on a set of xdg user dirs.

%prep
%setup -q
%patch0 -p1 -b .kde
%patch1 -p1 -b .mdkfolders

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
%find_lang %name

mkdir -p $RPM_BUILD_ROOT%{_datadir}/autostart
install -m644 user-dirs-update-gtk.desktop $RPM_BUILD_ROOT%{_datadir}/autostart

mkdir -p $RPM_BUILD_ROOT%_sysconfdir/X11/xinit.d
cat > $RPM_BUILD_ROOT%_sysconfdir/X11/xinit.d/xdg-user-dirs-update-gtk <<EOF
#!/bin/sh
DESKTOP=\$1
case \$DESKTOP in
   GNOME|KDE) exit 0;;
   *) exec /usr/bin/xdg-user-dirs-gtk-update ;;
esac
EOF

chmod +x $RPM_BUILD_ROOT%_sysconfdir/X11/xinit.d/xdg-user-dirs-update-gtk 

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %name.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog README NEWS
%config(noreplace) %_sysconfdir/xdg/autostart/user-dirs-update-gtk.desktop
%config(noreplace) %_sysconfdir/X11/xinit.d/xdg-user-dirs-update-gtk 
%_datadir/autostart/user-dirs-update-gtk.desktop
%_bindir/xdg-user-dirs-gtk-update
