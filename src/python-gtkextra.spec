Summary: Python bindings for the Gtk+Extra widget set.
Name: python-gtkextra2
Version: 1.1.0
Release: 1
Copyright: LGPL
Group: Development/Languages
Source: ftp://ftp.nowhere.org/pub/gtk/python/python-gtkextra-%{version}.tar.gz
BuildRoot: /var/tmp/python-gtkextra-root
Requires: gtk2 >= 1.3.9
Requires: python >= 2.2
Requires: pygtk2 >= 1.99.13
Requires: gtk+extra2 >= 1.1
Buildrequires: python-devel >= 2.2
Buildrequires: pygtk2-devel >= 1.99.13
Buildrequires: gtk+extra2-devel >= 1.1

%description
Python-gtkextra is an extension module for python that gives you access to
the Gtk+Extra widget set.

%package devel
Summary: files needed to build wrappers for python-gtkextra addon libraries
Group: Development/Languages
Requires: python-gtkextra2 = %{version}

%description devel
This package containes files needed to build wrappers for python-gtkextra
addon libraries so that they interoperate with python-gtkextra.

%prep
%setup -q -n python-gtkextra-%{version}
./configure --prefix=%{_prefix}

%build
make

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

%files
%defattr(644, root, root, 755)
%dir %{_prefix}/lib/python?.?/site-packages/gtk-2.0/gtkextra
%{_prefix}/lib/python?.?/site-packages/gtk-2.0/gtkextra/*.py*

%defattr(755, root, root, 755)
%{_prefix}/lib/python?.?/site-packages/gtk-2.0/gtkextra/_gtkextramodule.so

%doc AUTHORS NEWS README ChangeLog
%doc examples

%files devel
%defattr(755, root, root, 755)
%{_prefix}/lib/pkgconfig/python-gtkextra.pc
%{_prefix}/lib/python?.?/site-packages/gtk-2.0/gtkextra/_gtkextramodule.la
%dir %{_prefix}/share/pygtk/2.0/defs
%{_prefix}/share/pygtk/2.0/defs/gtkextra.defs
%{_prefix}/share/pygtk/2.0/defs/gtkextra-types.defs
%{_prefix}/share/pygtk/2.0/defs/gtkextra-addons.defs



