#
# Conditional build:
%bcond_without	tests	# unit tests
#
%define		pdir	Alien
%define		pnam	zlib
Summary:	Alien::zlib - Find or build zlib
Summary(pl.UTF-8):	Alien::zlib - znajdowanie lub budowanie biblioteki zlib
Name:		perl-Alien-zlib
Version:	0.02
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/modules/by-module/Alien/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	65a45611520915e2a297751722bf65b2
URL:		https://metacpan.org/dist/Alien-zlib
BuildRequires:	perl-Alien-Build >= 1.19
BuildRequires:	perl-ExtUtils-MakeMaker >= 6.52
BuildRequires:	perl-devel >= 1:5.8.4
BuildRequires:	pkgconfig
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl-Alien-Base >= 0.038
BuildRequires:	perl-Alien-Build >= 0.32
BuildRequires:	perl-Test-Alien
BuildRequires:	perl-Test-Simple
BuildRequires:	perl-Test2-Suite
%endif
BuildRequires:	zlib-devel
Requires:	perl-Alien-Base >= 0.038
Requires:	zlib-devel
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# no binary code, but platform dependent paths inside
%define		_enable_debug_packages	0

%description
This distribution provides zlib so that it can be used by other
Perl distributions that are on CPAN. It does this by first trying to
detect an existing install of zlib on your system. If found it will
use that. If it cannot be found, the source code will be downloaded
from the internet and it will be installed in a private share location
for the use of other modules.

%description -l pl.UTF-8
Ten pakiet dostarcza bibliotekę zlib tak, że może być używana przez
inne pakiety Perla z CPAN. W pierwszej kolejności próbuje wykryć
istniejącą instalację biblioteki zlib w systemie; jeśli nie istnieje,
zostanie pobrana i zainstalowana w prywatnej lokalizacji dla innych
modułów.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorarch}/Alien/zlib.pm
%{perl_vendorarch}/Alien/zlib
%{perl_vendorarch}/auto/Alien/zlib
%{perl_vendorarch}/auto/share/dist/Alien-zlib
%{_mandir}/man3/Alien::zlib.3pm*
