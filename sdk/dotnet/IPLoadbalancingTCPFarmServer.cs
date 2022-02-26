// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ovh
{
    /// <summary>
    /// Creates a backend server entry linked to loadbalancing group (farm)
    /// 
    /// ## Example Usage
    /// 
    /// ```csharp
    /// using Pulumi;
    /// using Ovh = Pulumi.Ovh;
    /// 
    /// class MyStack : Stack
    /// {
    ///     public MyStack()
    ///     {
    ///         var lb = Output.Create(Ovh.GetIPLoadbalancing.InvokeAsync(new Ovh.GetIPLoadbalancingArgs
    ///         {
    ///             ServiceName = "ip-1.2.3.4",
    ///             State = "ok",
    ///         }));
    ///         var farmname = new Ovh.IPLoadbalancingTCPFarm("farmname", new Ovh.IPLoadbalancingTCPFarmArgs
    ///         {
    ///             ServiceName = lb.Apply(lb =&gt; lb.Id),
    ///             Port = 8080,
    ///             Zone = "all",
    ///         });
    ///         var backend = new Ovh.IPLoadbalancingTCPFarmServer("backend", new Ovh.IPLoadbalancingTCPFarmServerArgs
    ///         {
    ///             ServiceName = lb.Apply(lb =&gt; lb.Id),
    ///             FarmId = farmname.Id,
    ///             DisplayName = "mybackend",
    ///             Address = "4.5.6.7",
    ///             Status = "active",
    ///             Port = 80,
    ///             ProxyProtocolVersion = v2,
    ///             Weight = 2,
    ///             Probe = true,
    ///             Ssl = false,
    ///             Backup = true,
    ///         });
    ///     }
    /// 
    /// }
    /// ```
    /// </summary>
    [OvhResourceType("ovh:index/iPLoadbalancingTCPFarmServer:IPLoadbalancingTCPFarmServer")]
    public partial class IPLoadbalancingTCPFarmServer : Pulumi.CustomResource
    {
        /// <summary>
        /// Address of the backend server (IP from either internal or OVH network)
        /// </summary>
        [Output("address")]
        public Output<string> Address { get; private set; } = null!;

        /// <summary>
        /// is it a backup server used in case of failure of all the non-backup backends
        /// </summary>
        [Output("backup")]
        public Output<bool?> Backup { get; private set; } = null!;

        [Output("chain")]
        public Output<string?> Chain { get; private set; } = null!;

        /// <summary>
        /// Label for the server
        /// </summary>
        [Output("displayName")]
        public Output<string?> DisplayName { get; private set; } = null!;

        /// <summary>
        /// ID of the farm this server is attached to
        /// </summary>
        [Output("farmId")]
        public Output<int> FarmId { get; private set; } = null!;

        /// <summary>
        /// Port that backend will respond on
        /// </summary>
        [Output("port")]
        public Output<int?> Port { get; private set; } = null!;

        /// <summary>
        /// defines if backend will be probed to determine health and keep as active in farm if healthy
        /// </summary>
        [Output("probe")]
        public Output<bool?> Probe { get; private set; } = null!;

        /// <summary>
        /// version of the PROXY protocol used to pass origin connection information from loadbalancer to recieving service (`v1`, `v2`, `v2-ssl`, `v2-ssl-cn`)
        /// </summary>
        [Output("proxyProtocolVersion")]
        public Output<string?> ProxyProtocolVersion { get; private set; } = null!;

        /// <summary>
        /// The internal name of your IP load balancing
        /// </summary>
        [Output("serviceName")]
        public Output<string> ServiceName { get; private set; } = null!;

        /// <summary>
        /// is the connection ciphered with SSL (TLS)
        /// </summary>
        [Output("ssl")]
        public Output<bool?> Ssl { get; private set; } = null!;

        /// <summary>
        /// backend status - `active` or `inactive`
        /// </summary>
        [Output("status")]
        public Output<string> Status { get; private set; } = null!;

        /// <summary>
        /// used in loadbalancing algorithm
        /// </summary>
        [Output("weight")]
        public Output<int?> Weight { get; private set; } = null!;


        /// <summary>
        /// Create a IPLoadbalancingTCPFarmServer resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public IPLoadbalancingTCPFarmServer(string name, IPLoadbalancingTCPFarmServerArgs args, CustomResourceOptions? options = null)
            : base("ovh:index/iPLoadbalancingTCPFarmServer:IPLoadbalancingTCPFarmServer", name, args ?? new IPLoadbalancingTCPFarmServerArgs(), MakeResourceOptions(options, ""))
        {
        }

        private IPLoadbalancingTCPFarmServer(string name, Input<string> id, IPLoadbalancingTCPFarmServerState? state = null, CustomResourceOptions? options = null)
            : base("ovh:index/iPLoadbalancingTCPFarmServer:IPLoadbalancingTCPFarmServer", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing IPLoadbalancingTCPFarmServer resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static IPLoadbalancingTCPFarmServer Get(string name, Input<string> id, IPLoadbalancingTCPFarmServerState? state = null, CustomResourceOptions? options = null)
        {
            return new IPLoadbalancingTCPFarmServer(name, id, state, options);
        }
    }

    public sealed class IPLoadbalancingTCPFarmServerArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Address of the backend server (IP from either internal or OVH network)
        /// </summary>
        [Input("address", required: true)]
        public Input<string> Address { get; set; } = null!;

        /// <summary>
        /// is it a backup server used in case of failure of all the non-backup backends
        /// </summary>
        [Input("backup")]
        public Input<bool>? Backup { get; set; }

        [Input("chain")]
        public Input<string>? Chain { get; set; }

        /// <summary>
        /// Label for the server
        /// </summary>
        [Input("displayName")]
        public Input<string>? DisplayName { get; set; }

        /// <summary>
        /// ID of the farm this server is attached to
        /// </summary>
        [Input("farmId", required: true)]
        public Input<int> FarmId { get; set; } = null!;

        /// <summary>
        /// Port that backend will respond on
        /// </summary>
        [Input("port")]
        public Input<int>? Port { get; set; }

        /// <summary>
        /// defines if backend will be probed to determine health and keep as active in farm if healthy
        /// </summary>
        [Input("probe")]
        public Input<bool>? Probe { get; set; }

        /// <summary>
        /// version of the PROXY protocol used to pass origin connection information from loadbalancer to recieving service (`v1`, `v2`, `v2-ssl`, `v2-ssl-cn`)
        /// </summary>
        [Input("proxyProtocolVersion")]
        public Input<string>? ProxyProtocolVersion { get; set; }

        /// <summary>
        /// The internal name of your IP load balancing
        /// </summary>
        [Input("serviceName", required: true)]
        public Input<string> ServiceName { get; set; } = null!;

        /// <summary>
        /// is the connection ciphered with SSL (TLS)
        /// </summary>
        [Input("ssl")]
        public Input<bool>? Ssl { get; set; }

        /// <summary>
        /// backend status - `active` or `inactive`
        /// </summary>
        [Input("status", required: true)]
        public Input<string> Status { get; set; } = null!;

        /// <summary>
        /// used in loadbalancing algorithm
        /// </summary>
        [Input("weight")]
        public Input<int>? Weight { get; set; }

        public IPLoadbalancingTCPFarmServerArgs()
        {
        }
    }

    public sealed class IPLoadbalancingTCPFarmServerState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Address of the backend server (IP from either internal or OVH network)
        /// </summary>
        [Input("address")]
        public Input<string>? Address { get; set; }

        /// <summary>
        /// is it a backup server used in case of failure of all the non-backup backends
        /// </summary>
        [Input("backup")]
        public Input<bool>? Backup { get; set; }

        [Input("chain")]
        public Input<string>? Chain { get; set; }

        /// <summary>
        /// Label for the server
        /// </summary>
        [Input("displayName")]
        public Input<string>? DisplayName { get; set; }

        /// <summary>
        /// ID of the farm this server is attached to
        /// </summary>
        [Input("farmId")]
        public Input<int>? FarmId { get; set; }

        /// <summary>
        /// Port that backend will respond on
        /// </summary>
        [Input("port")]
        public Input<int>? Port { get; set; }

        /// <summary>
        /// defines if backend will be probed to determine health and keep as active in farm if healthy
        /// </summary>
        [Input("probe")]
        public Input<bool>? Probe { get; set; }

        /// <summary>
        /// version of the PROXY protocol used to pass origin connection information from loadbalancer to recieving service (`v1`, `v2`, `v2-ssl`, `v2-ssl-cn`)
        /// </summary>
        [Input("proxyProtocolVersion")]
        public Input<string>? ProxyProtocolVersion { get; set; }

        /// <summary>
        /// The internal name of your IP load balancing
        /// </summary>
        [Input("serviceName")]
        public Input<string>? ServiceName { get; set; }

        /// <summary>
        /// is the connection ciphered with SSL (TLS)
        /// </summary>
        [Input("ssl")]
        public Input<bool>? Ssl { get; set; }

        /// <summary>
        /// backend status - `active` or `inactive`
        /// </summary>
        [Input("status")]
        public Input<string>? Status { get; set; }

        /// <summary>
        /// used in loadbalancing algorithm
        /// </summary>
        [Input("weight")]
        public Input<int>? Weight { get; set; }

        public IPLoadbalancingTCPFarmServerState()
        {
        }
    }
}
