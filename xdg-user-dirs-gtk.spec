Summary:	XDG user dirs support for GNOME/GTK+
Name:		xdg-user-dirs-gtk
Version:	0.12
Release:	1
License:	GPLv2+
Group:		Graphical desktop/GNOME
Url:		https://www.gnome.org/
Source0:	http://ftp.gnome.org/pub/gnome/sources/xdg-user-dirs-gtk/%{version}/%{name}-%{version}.tar.xz
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	xdg-user-dirs
BuildRequires:	intltool
BuildRequires:	meson
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
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS ChangeLog README NEWS
%config(noreplace) %{_sysconfdir}/xdg/autostart/user-dirs-update-gtk.desktop
%{_bindir}/xdg-user-dirs-gtk-update
