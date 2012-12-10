%define name	autounit
%define version	0.20.1
%define release	7
%define	major	2
%define	libname	%mklibname %{name} %{major}

Name:		    %{name}
Version:	    %{version}
Release:	    %{release}
License:	    GPL
Summary:	    C testing framework
Group:		    System/Libraries
URL:		    http://www.recursism.com/pub/software/testing/gnu-autounit
Source:		    http://www.recursism.com/pub/files/%{name}-%{version}.tar.bz2
BuildRequires:	glib-devel

%description
GNU Autounit's goal is to provide a common unit testing framework for
applications developers who use GNU Autoconf already in their products, but do
not currently use a unit testing framework.

%package -n	%{libname}
Summary:	C testing framework
Group:		System/Libraries

%description -n	%{libname}
GNU Autounit's goal is to provide a common unit testing framework for
applications developers who use GNU Autoconf already in their products, but do
not currently use a unit testing framework.

%package -n	%{libname}-devel 
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}

%description -n	%{libname}-devel
This package contains development files for %{name}.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std
rm -rf %{buildroot}%{_prefix}/doc
chmod 644  %{buildroot}%{_libdir}/*.la

%files -n %{libname}
%defattr(-,root,root)
%doc COPYING
%{_libdir}/*.so.*

%files -n %{libname}-devel
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README TODO
%{_libdir}/*.so
%{_libdir}/*.a
%{_includedir}/%{name}



%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 0.20.1-6mdv2011.0
+ Revision: 616669
- the mass rebuild of 2010.0 packages

* Wed Sep 02 2009 Thierry Vignaud <tv@mandriva.org> 0.20.1-5mdv2010.0
+ Revision: 424588
- use %%configure2_5x
- rebuild
- rebuild

* Thu Jun 19 2008 Thierry Vignaud <tv@mandriva.org> 0.20.1-3mdv2009.0
+ Revision: 226206
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue Dec 18 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.20.1-2mdv2008.1
+ Revision: 132392
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - import autounit


* Fri Sep 01 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.20.1-1mdv2007.0
- new version

* Tue Aug 29 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.15.2-5mdv2007.0
- Rebuild

* Thu May 04 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.15.2-4mdk
- fix lib64 build

* Mon Apr 17 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.15.2-3mdk
- fix major, wich mas mysteriously downgraded in latest release

* Fri Apr 14 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.15.2-2mdk
- buildrequires glib-devel

* Mon Mar 27 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.15.2-1mdk
- first mdk release
