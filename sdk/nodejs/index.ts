// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

// Export members:
export * from "./cloudNetworkPrivate";
export * from "./cloudNetworkPrivateSubnet";
export * from "./cloudUser";
export * from "./dedicatedCephACL";
export * from "./dedicatedServerInstallTask";
export * from "./dedicatedServerRebootTask";
export * from "./dedicatedServerUpdate";
export * from "./domainZoneRecord";
export * from "./domainZoneRedirection";
export * from "./getCloudRegion";
export * from "./getCloudRegions";
export * from "./getDedicatedCEPH";
export * from "./getDedicatedInstallationTemplates";
export * from "./getDedicatedServer";
export * from "./getDedicatedServerBoots";
export * from "./getDedicatedServers";
export * from "./getDomainZone";
export * from "./getIPLoadbalancing";
export * from "./getIPLoadbalancingVRACNetwork";
export * from "./getIPLoadbalancingVRACNetworks";
export * from "./getMeIPXEScript";
export * from "./getMeIPXEScripts";
export * from "./getMeInstallationTemplate";
export * from "./getMeInstallationTemplates";
export * from "./getMePaymentMeanBankAccount";
export * from "./getMePaymentMeanCreditCard";
export * from "./getMeSSHKey";
export * from "./getMeSSHKeys";
export * from "./getPublicCloudRegion";
export * from "./getPublicCloudRegions";
export * from "./getVPS";
export * from "./getVRACKS";
export * from "./iploadbalancingHTTPFarm";
export * from "./iploadbalancingHTTPFarmServer";
export * from "./iploadbalancingHTTPFrontend";
export * from "./iploadbalancingHTTPRoute";
export * from "./iploadbalancingHTTPRouteRule";
export * from "./iploadbalancingRefresh";
export * from "./iploadbalancingTCPFarm";
export * from "./iploadbalancingTCPFarmServer";
export * from "./iploadbalancingTCPFrontend";
export * from "./iploadbalancingVRACNetwork";
export * from "./ipreverse";
export * from "./meIPXEScript";
export * from "./meInstallationTemplate";
export * from "./meInstallationTemplatePartitionScheme";
export * from "./meInstallationTemplatePartitionSchemeHardwareRaid";
export * from "./meInstallationTemplatePartitionSchemePartition";
export * from "./meSSHKey";
export * from "./provider";
export * from "./pubicCloudPrivateNetwork";
export * from "./pubicCloudPrivateNetworkSubnet";
export * from "./publicCloudUser";
export * from "./vraccloudProject";
export * from "./vracdedicatedServer";
export * from "./vracdedicatedServerInterface";
export * from "./vraciploadbalancing";
export * from "./vracpublicCloudAttachment";

// Export sub-modules:
import * as config from "./config";
import * as types from "./types";

export {
    config,
    types,
};

// Import resources to register:
import { CloudNetworkPrivate } from "./cloudNetworkPrivate";
import { CloudNetworkPrivateSubnet } from "./cloudNetworkPrivateSubnet";
import { CloudUser } from "./cloudUser";
import { DedicatedCephACL } from "./dedicatedCephACL";
import { DedicatedServerInstallTask } from "./dedicatedServerInstallTask";
import { DedicatedServerRebootTask } from "./dedicatedServerRebootTask";
import { DedicatedServerUpdate } from "./dedicatedServerUpdate";
import { DomainZoneRecord } from "./domainZoneRecord";
import { DomainZoneRedirection } from "./domainZoneRedirection";
import { IPLoadbalancingHTTPFarm } from "./iploadbalancingHTTPFarm";
import { IPLoadbalancingHTTPFarmServer } from "./iploadbalancingHTTPFarmServer";
import { IPLoadbalancingHTTPFrontend } from "./iploadbalancingHTTPFrontend";
import { IPLoadbalancingHTTPRoute } from "./iploadbalancingHTTPRoute";
import { IPLoadbalancingHTTPRouteRule } from "./iploadbalancingHTTPRouteRule";
import { IPLoadbalancingRefresh } from "./iploadbalancingRefresh";
import { IPLoadbalancingTCPFarm } from "./iploadbalancingTCPFarm";
import { IPLoadbalancingTCPFarmServer } from "./iploadbalancingTCPFarmServer";
import { IPLoadbalancingTCPFrontend } from "./iploadbalancingTCPFrontend";
import { IPLoadbalancingVRACNetwork } from "./iploadbalancingVRACNetwork";
import { IPReverse } from "./ipreverse";
import { MeIPXEScript } from "./meIPXEScript";
import { MeInstallationTemplate } from "./meInstallationTemplate";
import { MeInstallationTemplatePartitionScheme } from "./meInstallationTemplatePartitionScheme";
import { MeInstallationTemplatePartitionSchemeHardwareRaid } from "./meInstallationTemplatePartitionSchemeHardwareRaid";
import { MeInstallationTemplatePartitionSchemePartition } from "./meInstallationTemplatePartitionSchemePartition";
import { MeSSHKey } from "./meSSHKey";
import { PubicCloudPrivateNetwork } from "./pubicCloudPrivateNetwork";
import { PubicCloudPrivateNetworkSubnet } from "./pubicCloudPrivateNetworkSubnet";
import { PublicCloudUser } from "./publicCloudUser";
import { VRACCloudProject } from "./vraccloudProject";
import { VRACDedicatedServer } from "./vracdedicatedServer";
import { VRACDedicatedServerInterface } from "./vracdedicatedServerInterface";
import { VRACIPLoadbalancing } from "./vraciploadbalancing";
import { VRACPublicCloudAttachment } from "./vracpublicCloudAttachment";

const _module = {
    version: utilities.getVersion(),
    construct: (name: string, type: string, urn: string): pulumi.Resource => {
        switch (type) {
            case "ovh:index/cloudNetworkPrivate:CloudNetworkPrivate":
                return new CloudNetworkPrivate(name, <any>undefined, { urn })
            case "ovh:index/cloudNetworkPrivateSubnet:CloudNetworkPrivateSubnet":
                return new CloudNetworkPrivateSubnet(name, <any>undefined, { urn })
            case "ovh:index/cloudUser:CloudUser":
                return new CloudUser(name, <any>undefined, { urn })
            case "ovh:index/dedicatedCephACL:DedicatedCephACL":
                return new DedicatedCephACL(name, <any>undefined, { urn })
            case "ovh:index/dedicatedServerInstallTask:DedicatedServerInstallTask":
                return new DedicatedServerInstallTask(name, <any>undefined, { urn })
            case "ovh:index/dedicatedServerRebootTask:DedicatedServerRebootTask":
                return new DedicatedServerRebootTask(name, <any>undefined, { urn })
            case "ovh:index/dedicatedServerUpdate:DedicatedServerUpdate":
                return new DedicatedServerUpdate(name, <any>undefined, { urn })
            case "ovh:index/domainZoneRecord:DomainZoneRecord":
                return new DomainZoneRecord(name, <any>undefined, { urn })
            case "ovh:index/domainZoneRedirection:DomainZoneRedirection":
                return new DomainZoneRedirection(name, <any>undefined, { urn })
            case "ovh:index/iPLoadbalancingHTTPFarm:IPLoadbalancingHTTPFarm":
                return new IPLoadbalancingHTTPFarm(name, <any>undefined, { urn })
            case "ovh:index/iPLoadbalancingHTTPFarmServer:IPLoadbalancingHTTPFarmServer":
                return new IPLoadbalancingHTTPFarmServer(name, <any>undefined, { urn })
            case "ovh:index/iPLoadbalancingHTTPFrontend:IPLoadbalancingHTTPFrontend":
                return new IPLoadbalancingHTTPFrontend(name, <any>undefined, { urn })
            case "ovh:index/iPLoadbalancingHTTPRoute:IPLoadbalancingHTTPRoute":
                return new IPLoadbalancingHTTPRoute(name, <any>undefined, { urn })
            case "ovh:index/iPLoadbalancingHTTPRouteRule:IPLoadbalancingHTTPRouteRule":
                return new IPLoadbalancingHTTPRouteRule(name, <any>undefined, { urn })
            case "ovh:index/iPLoadbalancingRefresh:IPLoadbalancingRefresh":
                return new IPLoadbalancingRefresh(name, <any>undefined, { urn })
            case "ovh:index/iPLoadbalancingTCPFarm:IPLoadbalancingTCPFarm":
                return new IPLoadbalancingTCPFarm(name, <any>undefined, { urn })
            case "ovh:index/iPLoadbalancingTCPFarmServer:IPLoadbalancingTCPFarmServer":
                return new IPLoadbalancingTCPFarmServer(name, <any>undefined, { urn })
            case "ovh:index/iPLoadbalancingTCPFrontend:IPLoadbalancingTCPFrontend":
                return new IPLoadbalancingTCPFrontend(name, <any>undefined, { urn })
            case "ovh:index/iPLoadbalancingVRACNetwork:IPLoadbalancingVRACNetwork":
                return new IPLoadbalancingVRACNetwork(name, <any>undefined, { urn })
            case "ovh:index/iPReverse:IPReverse":
                return new IPReverse(name, <any>undefined, { urn })
            case "ovh:index/meIPXEScript:MeIPXEScript":
                return new MeIPXEScript(name, <any>undefined, { urn })
            case "ovh:index/meInstallationTemplate:MeInstallationTemplate":
                return new MeInstallationTemplate(name, <any>undefined, { urn })
            case "ovh:index/meInstallationTemplatePartitionScheme:MeInstallationTemplatePartitionScheme":
                return new MeInstallationTemplatePartitionScheme(name, <any>undefined, { urn })
            case "ovh:index/meInstallationTemplatePartitionSchemeHardwareRaid:MeInstallationTemplatePartitionSchemeHardwareRaid":
                return new MeInstallationTemplatePartitionSchemeHardwareRaid(name, <any>undefined, { urn })
            case "ovh:index/meInstallationTemplatePartitionSchemePartition:MeInstallationTemplatePartitionSchemePartition":
                return new MeInstallationTemplatePartitionSchemePartition(name, <any>undefined, { urn })
            case "ovh:index/meSSHKey:MeSSHKey":
                return new MeSSHKey(name, <any>undefined, { urn })
            case "ovh:index/pubicCloudPrivateNetwork:PubicCloudPrivateNetwork":
                return new PubicCloudPrivateNetwork(name, <any>undefined, { urn })
            case "ovh:index/pubicCloudPrivateNetworkSubnet:PubicCloudPrivateNetworkSubnet":
                return new PubicCloudPrivateNetworkSubnet(name, <any>undefined, { urn })
            case "ovh:index/publicCloudUser:PublicCloudUser":
                return new PublicCloudUser(name, <any>undefined, { urn })
            case "ovh:index/vRACCloudProject:VRACCloudProject":
                return new VRACCloudProject(name, <any>undefined, { urn })
            case "ovh:index/vRACDedicatedServer:VRACDedicatedServer":
                return new VRACDedicatedServer(name, <any>undefined, { urn })
            case "ovh:index/vRACDedicatedServerInterface:VRACDedicatedServerInterface":
                return new VRACDedicatedServerInterface(name, <any>undefined, { urn })
            case "ovh:index/vRACIPLoadbalancing:VRACIPLoadbalancing":
                return new VRACIPLoadbalancing(name, <any>undefined, { urn })
            case "ovh:index/vRACPublicCloudAttachment:VRACPublicCloudAttachment":
                return new VRACPublicCloudAttachment(name, <any>undefined, { urn })
            default:
                throw new Error(`unknown resource type ${type}`);
        }
    },
};
pulumi.runtime.registerResourceModule("ovh", "index/cloudNetworkPrivate", _module)
pulumi.runtime.registerResourceModule("ovh", "index/cloudNetworkPrivateSubnet", _module)
pulumi.runtime.registerResourceModule("ovh", "index/cloudUser", _module)
pulumi.runtime.registerResourceModule("ovh", "index/dedicatedCephACL", _module)
pulumi.runtime.registerResourceModule("ovh", "index/dedicatedServerInstallTask", _module)
pulumi.runtime.registerResourceModule("ovh", "index/dedicatedServerRebootTask", _module)
pulumi.runtime.registerResourceModule("ovh", "index/dedicatedServerUpdate", _module)
pulumi.runtime.registerResourceModule("ovh", "index/domainZoneRecord", _module)
pulumi.runtime.registerResourceModule("ovh", "index/domainZoneRedirection", _module)
pulumi.runtime.registerResourceModule("ovh", "index/iPLoadbalancingHTTPFarm", _module)
pulumi.runtime.registerResourceModule("ovh", "index/iPLoadbalancingHTTPFarmServer", _module)
pulumi.runtime.registerResourceModule("ovh", "index/iPLoadbalancingHTTPFrontend", _module)
pulumi.runtime.registerResourceModule("ovh", "index/iPLoadbalancingHTTPRoute", _module)
pulumi.runtime.registerResourceModule("ovh", "index/iPLoadbalancingHTTPRouteRule", _module)
pulumi.runtime.registerResourceModule("ovh", "index/iPLoadbalancingRefresh", _module)
pulumi.runtime.registerResourceModule("ovh", "index/iPLoadbalancingTCPFarm", _module)
pulumi.runtime.registerResourceModule("ovh", "index/iPLoadbalancingTCPFarmServer", _module)
pulumi.runtime.registerResourceModule("ovh", "index/iPLoadbalancingTCPFrontend", _module)
pulumi.runtime.registerResourceModule("ovh", "index/iPLoadbalancingVRACNetwork", _module)
pulumi.runtime.registerResourceModule("ovh", "index/iPReverse", _module)
pulumi.runtime.registerResourceModule("ovh", "index/meIPXEScript", _module)
pulumi.runtime.registerResourceModule("ovh", "index/meInstallationTemplate", _module)
pulumi.runtime.registerResourceModule("ovh", "index/meInstallationTemplatePartitionScheme", _module)
pulumi.runtime.registerResourceModule("ovh", "index/meInstallationTemplatePartitionSchemeHardwareRaid", _module)
pulumi.runtime.registerResourceModule("ovh", "index/meInstallationTemplatePartitionSchemePartition", _module)
pulumi.runtime.registerResourceModule("ovh", "index/meSSHKey", _module)
pulumi.runtime.registerResourceModule("ovh", "index/pubicCloudPrivateNetwork", _module)
pulumi.runtime.registerResourceModule("ovh", "index/pubicCloudPrivateNetworkSubnet", _module)
pulumi.runtime.registerResourceModule("ovh", "index/publicCloudUser", _module)
pulumi.runtime.registerResourceModule("ovh", "index/vRACCloudProject", _module)
pulumi.runtime.registerResourceModule("ovh", "index/vRACDedicatedServer", _module)
pulumi.runtime.registerResourceModule("ovh", "index/vRACDedicatedServerInterface", _module)
pulumi.runtime.registerResourceModule("ovh", "index/vRACIPLoadbalancing", _module)
pulumi.runtime.registerResourceModule("ovh", "index/vRACPublicCloudAttachment", _module)

import { Provider } from "./provider";

pulumi.runtime.registerResourcePackage("ovh", {
    version: utilities.getVersion(),
    constructProvider: (name: string, type: string, urn: string): pulumi.ProviderResource => {
        if (type !== "pulumi:providers:ovh") {
            throw new Error(`unknown provider type ${type}`);
        }
        return new Provider(name, <any>undefined, { urn });
    },
});
