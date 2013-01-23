Summary:	XDG user dirs support for GNOME/GTK+
Name:		xdg-user-dirs-gtk
Version:	0.10
Release:	1
License:	GPLv2+
Group:		Graphical desktop/GNOME
Url:		http://www.gnome.org/
Source0:	http://ftp.gnome.org/pub/gnome/sources/xdg-user-dirs-gtk/%{version}/%{name}-%{version}.tar.xz
BuildRequires:	gtk+3-devel
BuildRequires:	xdg-user-dirs
BuildRequires:	intltool
Requires:	xdg-user-dirs

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

%build
sed -i \
	-e '/Encoding/d' \
	-e 's:OnlyShowIn=GNOME;LXDE;Unity;:NotShowIn=KDE;:' \
	user-dirs-update-gtk.desktop.in || die

%configure2_5x
%make

%install
%makeinstall_std

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS ChangeLog README NEWS
%config(noreplace) %{_sysconfdir}/xdg/autostart/user-dirs-update-gtk.desktop
%{_bindir}/xdg-user-dirs-gtk-update


%changelog
* Sat May 07 2011 Oden Eriksson <oeriksson@mandriva.com> 0.8-11mdv2011.0
+ Revision: 671294
- mass rebuild

* Sat Feb 26 2011 Funda Wang <fwang@mandriva.org> 0.8-10
+ Revision: 639993
- rebuild

* Wed Feb 16 2011 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 0.8-9
+ Revision: 638068
- Remove xinit.d script: old WMs should use xdg-compliance-autostart

* Fri Feb 04 2011 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 0.8-8
+ Revision: 635783
- Remove /usr/share/autostart copy, since only KDE runs it and it also supports
  the standard /etc/xdg/autostart script
- Add LXDE to "skip" list since it supports /etc/xdg/autostart
- Fix kde patch so it doesn't generate a desktop file with duplicated entries.
  According to the spec:
  "Multiple keys in the same group may not have the same name."

* Wed Jan 19 2011 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 0.8-6
+ Revision: 631677
- Fix xinit.d string for KDE
  So we don't run the script twice under KDE4: one for xinit.d and one for xdg
  autostart. Faster login!

* Sat Dec 04 2010 Oden Eriksson <oeriksson@mandriva.com> 0.8-5mdv2011.0
+ Revision: 608198
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 0.8-4mdv2010.1
+ Revision: 524412
- rebuilt for 2010.1

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 0.8-3mdv2009.1
+ Revision: 351209
- rebuild

* Fri Sep 19 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.8-2mdv2009.0
+ Revision: 285918
- new license policy
- get rid of redefines
- update urls
- spec file clean

* Sat Sep 06 2008 Götz Waschk <waschk@mandriva.org> 0.8-1mdv2009.0
+ Revision: 281926
- fix buildrequires
- new version

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 0.7-3mdv2009.0
+ Revision: 226027
- rebuild

* Mon Mar 17 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.7-2mdv2008.1
+ Revision: 188407
- add support for Xfce
- spec file clean

* Tue Feb 12 2008 Götz Waschk <waschk@mandriva.org> 0.7-1mdv2008.1
+ Revision: 165918
- new version
- rediff patch 0

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Sep 28 2007 Frederic Crozat <fcrozat@mandriva.com> 0.6-2mdv2008.0
+ Revision: 93665
- Update patch1 to fix crash on x86-64 (we were lucky it didn't crash on x86, it should have), bug report from Francois Bandet

* Tue Aug 21 2007 Götz Waschk <waschk@mandriva.org> 0.6-1mdv2008.0
+ Revision: 68371
- new version

* Fri Aug 03 2007 Frederic Crozat <fcrozat@mandriva.com> 0.5-2mdv2008.0
+ Revision: 58610
- Patch0: add KDE info to desktop file
- Patch1: detect mdk-folders entries in gtk-bookmarks and replace them with standard entries ; remove .directories in those mdk folders when translations changes
- add xinit.d script for desktop environment not support XDG autostart

* Mon May 14 2007 Götz Waschk <waschk@mandriva.org> 0.5-1mdv2008.0
+ Revision: 26652
- new version

* Tue Apr 17 2007 Götz Waschk <waschk@mandriva.org> 0.4-1mdv2008.0
+ Revision: 14169
- fix buildrequires
- Import xdg-user-dirs-gtk



* Wed Apr 11 2007 Götz Waschk <waschk@mandriva.org> 0.4-1mdv2007.1
- initial package
