%define perlvendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)

Name:           perl-Newt
Version:        1.08
Release:	5
Summary:        Edit configuration files through Augeas C library
License:        Artistic
Group:          System/Configuration/Other
URL:            https://search.cpan.org/dist/Newt
Source0:        http://search.cpan.org/CPAN/authors/id/A/AM/AMEDINA/Newt-1.08.tar.gz
Patch0:			newt-perl-1.08-debian.patch
Patch1:			newt-perl-1.08-typemap.patch
Patch2:			newt-perl-1.08-fix.patch
Patch3:			newt-perl-1.08-xs.patch
Patch4:			newt-perl-1.08-lang.patch
Patch5:			perl-Newt-bz385751.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  perl-devel,newt-devel,popt-devel

%description
Perl bindings for RedHat newt library

%prep
%setup -q -n Newt-%{version}
%patch0 -p1 -b .debian
%patch1 -p1 -b .valist
%patch2 -p1 -b .fix
%patch3 -p1 -b .exes
%patch4 -p1 -b .lang
%patch5 -p1 -b .bz385751
rm -rf newtlib

%build
%{__perl} Makefile.PL PREFIX=%{_prefix} INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
make

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT
find ${RPM_BUILD_ROOT} -type f -name perllocal.pod -o -name .packlist -o -name '*.bs' -a -size 0 | xargs rm -f
find ${RPM_BUILD_ROOT} -type d -depth | xargs rmdir --ignore-fail-on-non-empty

#%{_fixperms} $RPM_BUILD_ROOT/*

%check
#make test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc ChangeLog README
%{perlvendorlib}/*
%{_mandir}/man3/*


%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.08-3
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Wed Aug 26 2009 Bruno Cornec <bcornec@mandriva.org> 1.08-2mdv2010.0
+ Revision: 421312
- Update to fedora -22 version to remove a AUTOLOAD warning with an additional patch

* Sat Aug 22 2009 Bruno Cornec <bcornec@mandriva.org> 1.08-1mdv2010.0
+ Revision: 419436
- Initial import based on Fedora package
- create perl-Newt

