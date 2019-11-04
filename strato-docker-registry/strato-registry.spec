Name:           strato-registry
Version:        1.0
Release:        1%{?dist}
License:        Stratoscale
Summary:        Stratoscale Registry Files

%description
Files needed for strato's docker registry service.

%build
cp $TOP/strato-docker-registry/docker-registry.service .
cp $TOP/strato-docker-registry/docker-registry.service.clustermanager .
cp $TOP/strato-docker-registry/docker-registry.yml .

%install
install -d %{buildroot}/etc/stratoscale/compose/rootfs-star/
install -pm 644 docker-registry.yml %{buildroot}/etc/stratoscale/compose/rootfs-star/
install -d %{buildroot}/usr/lib/systemd/system
install -pm 644 docker-registry.service %{buildroot}/usr/lib/systemd/system/
install -d %{buildroot}/etc/stratoscale/clustermanager/services/control/
install -pm 644 docker-registry.service.clustermanager %{buildroot}/etc/stratoscale/clustermanager/services/control/docker-registry.service

%files
/usr/lib/systemd/system/docker-registry.service
/etc/stratoscale/clustermanager/services/control/docker-registry.service
/etc/stratoscale/compose/rootfs-star/docker-registry.yml
