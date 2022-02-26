// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ovh
{
    public static class GetVPS
    {
        /// <summary>
        /// Use this data source to retrieve information about a vps associated with 
        /// your OVH Account.
        /// 
        /// {{% examples %}}
        /// ## Example Usage
        /// {{% example %}}
        /// 
        /// ```csharp
        /// using Pulumi;
        /// using Ovh = Pulumi.Ovh;
        /// 
        /// class MyStack : Stack
        /// {
        ///     public MyStack()
        ///     {
        ///         var server = Output.Create(Ovh.GetVPS.InvokeAsync(new Ovh.GetVPSArgs
        ///         {
        ///             ServiceName = "XXXXXX",
        ///         }));
        ///     }
        /// 
        /// }
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Task<GetVPSResult> InvokeAsync(GetVPSArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetVPSResult>("ovh:index/getVPS:getVPS", args ?? new GetVPSArgs(), options.WithDefaults());

        /// <summary>
        /// Use this data source to retrieve information about a vps associated with 
        /// your OVH Account.
        /// 
        /// {{% examples %}}
        /// ## Example Usage
        /// {{% example %}}
        /// 
        /// ```csharp
        /// using Pulumi;
        /// using Ovh = Pulumi.Ovh;
        /// 
        /// class MyStack : Stack
        /// {
        ///     public MyStack()
        ///     {
        ///         var server = Output.Create(Ovh.GetVPS.InvokeAsync(new Ovh.GetVPSArgs
        ///         {
        ///             ServiceName = "XXXXXX",
        ///         }));
        ///     }
        /// 
        /// }
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Output<GetVPSResult> Invoke(GetVPSInvokeArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetVPSResult>("ovh:index/getVPS:getVPS", args ?? new GetVPSInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetVPSArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// The service_name of your dedicated server.
        /// </summary>
        [Input("serviceName", required: true)]
        public string ServiceName { get; set; } = null!;

        public GetVPSArgs()
        {
        }
    }

    public sealed class GetVPSInvokeArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// The service_name of your dedicated server.
        /// </summary>
        [Input("serviceName", required: true)]
        public Input<string> ServiceName { get; set; } = null!;

        public GetVPSInvokeArgs()
        {
        }
    }


    [OutputType]
    public sealed class GetVPSResult
    {
        /// <summary>
        /// The ovh cluster the vps is in
        /// </summary>
        public readonly string Cluster;
        /// <summary>
        /// The datacenter in which the vps is located
        /// * `datacenter.longname` - The fullname of the datacenter (ex: "Strasbourg SBG1")
        /// * `datacenter.name` - The short name of the datacenter (ex: "sbg1)
        /// </summary>
        public readonly ImmutableArray<Outputs.GetVPSDatacenterResult> Datacenters;
        /// <summary>
        /// The displayed name in the ovh web admin
        /// </summary>
        public readonly string Displayname;
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        /// <summary>
        /// The list of IPs addresses attached to the vps
        /// </summary>
        public readonly ImmutableArray<string> Ips;
        /// <summary>
        /// The keymap for the ip kvm, valid values "", "fr", "us"
        /// </summary>
        public readonly string Keymap;
        /// <summary>
        /// The amount of memory in MB of the vps.
        /// </summary>
        public readonly int Memory;
        /// <summary>
        /// A dict describing the type of vps.
        /// * `model.name` - The model name (ex: model1)
        /// * `model.offer` - The model human description (ex: "VPS 2016 SSD 1")
        /// * `model.version` - The model version (ex: "2017v2")
        /// </summary>
        public readonly ImmutableArray<Outputs.GetVPSModelResult> Models;
        public readonly string Name;
        /// <summary>
        /// The source of the boot kernel
        /// </summary>
        public readonly string Netbootmode;
        /// <summary>
        /// The type of offer (ssd, cloud, classic)
        /// </summary>
        public readonly string Offertype;
        public readonly string ServiceName;
        /// <summary>
        /// A boolean to indicate if OVH sla monitoring is active.
        /// </summary>
        public readonly bool Slamonitoring;
        /// <summary>
        /// The state of the vps
        /// </summary>
        public readonly string State;
        /// <summary>
        /// The type of server
        /// </summary>
        public readonly string Type;
        /// <summary>
        /// The number of vcore of the vps
        /// </summary>
        public readonly int Vcore;
        /// <summary>
        /// The OVH zone where the vps is
        /// </summary>
        public readonly string Zone;

        [OutputConstructor]
        private GetVPSResult(
            string cluster,

            ImmutableArray<Outputs.GetVPSDatacenterResult> datacenters,

            string displayname,

            string id,

            ImmutableArray<string> ips,

            string keymap,

            int memory,

            ImmutableArray<Outputs.GetVPSModelResult> models,

            string name,

            string netbootmode,

            string offertype,

            string serviceName,

            bool slamonitoring,

            string state,

            string type,

            int vcore,

            string zone)
        {
            Cluster = cluster;
            Datacenters = datacenters;
            Displayname = displayname;
            Id = id;
            Ips = ips;
            Keymap = keymap;
            Memory = memory;
            Models = models;
            Name = name;
            Netbootmode = netbootmode;
            Offertype = offertype;
            ServiceName = serviceName;
            Slamonitoring = slamonitoring;
            State = state;
            Type = type;
            Vcore = vcore;
            Zone = zone;
        }
    }
}