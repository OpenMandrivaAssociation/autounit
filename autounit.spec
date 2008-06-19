%define name	autounit
%define version	0.20.1
%define release	%mkrel 3
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
BuildRoot:	    %{_tmppath}/%{name}-%{version}

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
%configure
%make

%install
rm -rf %{buildroot}
%makeinstall_std
rm -rf %{buildroot}%{_prefix}/doc
chmod 644  %{buildroot}%{_libdir}/*.la

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%doc COPYING
%{_libdir}/*.so.*

%files -n %{libname}-devel
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README TODO
%{_libdir}/*.la
%{_libdir}/*.so
%{_libdir}/*.a
%{_includedir}/%{name}

