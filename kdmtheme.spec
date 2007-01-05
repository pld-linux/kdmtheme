Summary:	KDM Theme Settings Module
Summary(pl):	Modu³ ustawieñ motywów KDM
Name:		kdmtheme
Version:	1.1.2
Release:	1
License:	GPL 
Group:		Applications
Source0:	http://beta.smileaf.org/files/kdmtheme/%{name}-%{version}.tar.bz2
# Source0-md5:	40bacda700e847aab7070babc15f67ca
URL:		http://www.kde-look.org/content/show.php?content=22120
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	kdelibs-devel >= 9:3.4.0
BuildRequires:	rpmbuild(macros) >= 1.129
Requires:	kdm >= 9:3.4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This control module allows you to easily add, remove and select any
KDM theme you want.

%description -l pl
Ten modu³ ustawieñ pozwala na ³atwe zarz±dzanie motywami KDM.
 
%prep
%setup -q

%build
cp -f /usr/share/automake/config.sub admin

mv admin/cvs.sh admin/cvs.sh.bak
cat admin/cvs.sh.bak | \
     sed 's:utoconf\*2\.5\*:utoconf*:g' | \
     sed 's:utoheader\*2\.5\*:utoheader*:g' | \
     sed 's:automake\*1\.6\.\*:automake*1.*:g' | \
     > admin/cvs.sh

%{__make} -f admin/Makefile.common cvs

%configure \
%if "%{_lib}" == "lib64"
	--enable-libsuffix=64 \
%endif
	--%{?debug:en}%{!?debug:dis}able-debug%{?debug:=full} \
	--with-qt-libraries=%{_libdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_pixmapsdir},%{_desktopdir}} \
	$RPM_BUILD_ROOT%{_datadir}/config/kdm

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir} \
	kde_libs_htmldir=%{_kdedocdir} \
	kdelnkdir=%{_desktopdir} \

%find_lang %{name} --with-kde

#shortcut to make kdmtheme applet work
ln -sf %{_sysconfdir}/X11/kdm/kdmrc $RPM_BUILD_ROOT%{_datadir}/config/kdm/kdmrc

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/kcm_kdmtheme.so
%{_libdir}/kde3/kcm_kdmtheme.la
%{_desktopdir}/kde/kdmtheme.desktop
%{_datadir}/config/kdm
