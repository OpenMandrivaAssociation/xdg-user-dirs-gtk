Summary:	XDG user dirs support for GNOME/GTK+
Name:		xdg-user-dirs-gtk
Version:	0.10
Release:	12
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

%configure
%make

%install
%makeinstall_std

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS ChangeLog README NEWS
%config(noreplace) %{_sysconfdir}/xdg/autostart/user-dirs-update-gtk.desktop
%{_bindir}/xdg-user-dirs-gtk-update
