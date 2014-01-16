%{?_javapackages_macros:%_javapackages_macros}
%global git e55ca83

%global namedreltag -SNAPSHOT
%global namedversion %{version}%{?namedreltag}

Name: coro-mock
Version: 1.0
Release: 0.4.%{git}git.0%{?dist}
Summary: A mock library for compiling JVM coroutine-using code on JVMs without coroutines

License: Public Domain
Url: https://github.com/headius/coro-mock
Source0: https://github.com/headius/%{name}/tarball/%{git}/headius-%{name}-%{git}.tar.gz

BuildRequires: forge-parent
BuildRequires: java-devel
BuildRequires: jpackage-utils
BuildRequires: junit

BuildRequires: maven-local
BuildRequires: maven-compiler-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin

Requires: java
Requires: jpackage-utils

BuildArch: noarch

%description
A small mock library for compiling JVM coroutine-utilizing code on JVMs
without coroutines.

%package javadoc

Summary: Javadoc for %{name}
Requires: jpackage-utils

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n headius-%{name}-%{git}

%build
mvn-rpmbuild install javadoc:aggregate

%install
mkdir -p %{buildroot}%{_javadir}
install -pm 644 target/%{name}-%{namedversion}.jar %{buildroot}%{_javadir}/%{name}.jar

mkdir -p %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml  %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar

mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -rp target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}

%files
%doc LICENSE
%{_javadir}/%{name}.jar
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%doc LICENSE
%{_javadocdir}/%{name}


%changelog
* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.4.e55ca83git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 22 2013 Bohuslav Kabrda <bkabrda@redhat.com> - 1.0-0.3.e55ca83git
- Reverted to old maven packaging standards. *sigh*

* Thu Feb 21 2013 Bohuslav Kabrda <bkabrda@redhat.com> - 1.0-0.2.e55ca83git
- Adapted to new maven packaging standards.

* Tue May 22 2012 Vít Ondruch <vondruch@redhat.com> - 1.0-0.1.e55ca83git
- Adapted from Mageia.

* Sat Feb 25 2012 gil <gil> 1.0-1.mga2
+ Revision: 214942
- imported package coro-mock
