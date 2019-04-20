#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Test-Inter
Version  : 1.09
Release  : 9
URL      : https://cpan.metacpan.org/authors/id/S/SB/SBECK/Test-Inter-1.09.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/S/SB/SBECK/Test-Inter-1.09.tar.gz
Summary  : Framework for more readable interactive test scripts
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Test-Inter-license = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(File::Find::Rule)
BuildRequires : perl(Test::Pod)
BuildRequires : perl(Test::Pod::Coverage)

%description
NAME
Test::Inter - framework for more readable interactive test scripts
DESCRIPTION
This is another framework for writing test scripts. Much of the syntax
is loosely inspired by Test::More, and Test::Inter has most of it's
functionality, but it is not a drop-in replacement.

%package dev
Summary: dev components for the perl-Test-Inter package.
Group: Development
Provides: perl-Test-Inter-devel = %{version}-%{release}
Requires: perl-Test-Inter = %{version}-%{release}

%description dev
dev components for the perl-Test-Inter package.


%package license
Summary: license components for the perl-Test-Inter package.
Group: Default

%description license
license components for the perl-Test-Inter package.


%prep
%setup -q -n Test-Inter-1.09

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Test-Inter
cp LICENSE %{buildroot}/usr/share/package-licenses/perl-Test-Inter/LICENSE
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.2/Test/Inter.pm
/usr/lib/perl5/vendor_perl/5.28.2/Test/Inter.pod

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Test::Inter.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Test-Inter/LICENSE
