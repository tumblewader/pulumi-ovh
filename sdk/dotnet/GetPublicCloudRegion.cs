// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ovh
{
    public static class GetPublicCloudRegion
    {
        /// <summary>
        /// &gt; __DEPRECATED:__ Use `ovh.getCloudRegion` instead.
        /// 
        /// Use this data source to retrieve information about a region associated with a
        /// public cloud project. The region must be associated with the project.
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
        ///         var gRA1 = Output.Create(Ovh.GetPublicCloudRegion.InvokeAsync(new Ovh.GetPublicCloudRegionArgs
        ///         {
        ///             ProjectId = "XXXXXX",
        ///             Region = "GRA1",
        ///         }));
        ///     }
        /// 
        /// }
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Task<GetPublicCloudRegionResult> InvokeAsync(GetPublicCloudRegionArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetPublicCloudRegionResult>("ovh:index/getPublicCloudRegion:getPublicCloudRegion", args ?? new GetPublicCloudRegionArgs(), options.WithDefaults());

        /// <summary>
        /// &gt; __DEPRECATED:__ Use `ovh.getCloudRegion` instead.
        /// 
        /// Use this data source to retrieve information about a region associated with a
        /// public cloud project. The region must be associated with the project.
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
        ///         var gRA1 = Output.Create(Ovh.GetPublicCloudRegion.InvokeAsync(new Ovh.GetPublicCloudRegionArgs
        ///         {
        ///             ProjectId = "XXXXXX",
        ///             Region = "GRA1",
        ///         }));
        ///     }
        /// 
        /// }
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Output<GetPublicCloudRegionResult> Invoke(GetPublicCloudRegionInvokeArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetPublicCloudRegionResult>("ovh:index/getPublicCloudRegion:getPublicCloudRegion", args ?? new GetPublicCloudRegionInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetPublicCloudRegionArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// the name of the public cloud service
        /// </summary>
        [Input("name", required: true)]
        public string Name { get; set; } = null!;

        /// <summary>
        /// The id of the public cloud project. If omitted,
        /// the `OVH_PROJECT_ID` environment variable is used.
        /// </summary>
        [Input("projectId", required: true)]
        public string ProjectId { get; set; } = null!;

        public GetPublicCloudRegionArgs()
        {
        }
    }

    public sealed class GetPublicCloudRegionInvokeArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// the name of the public cloud service
        /// </summary>
        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        /// <summary>
        /// The id of the public cloud project. If omitted,
        /// the `OVH_PROJECT_ID` environment variable is used.
        /// </summary>
        [Input("projectId", required: true)]
        public Input<string> ProjectId { get; set; } = null!;

        public GetPublicCloudRegionInvokeArgs()
        {
        }
    }


    [OutputType]
    public sealed class GetPublicCloudRegionResult
    {
        /// <summary>
        /// the code of the geographic continent the region is running.
        /// E.g.: EU for Europe, US for America...
        /// </summary>
        public readonly string ContinentCode;
        /// <summary>
        /// The location code of the datacenter.
        /// E.g.: "GRA", meaning Gravelines, for region "GRA1"
        /// </summary>
        public readonly string DatacenterLocation;
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        /// <summary>
        /// the name of the public cloud service
        /// </summary>
        public readonly string Name;
        public readonly string ProjectId;
        /// <summary>
        /// The list of public cloud services running within the region
        /// </summary>
        public readonly ImmutableArray<Outputs.GetPublicCloudRegionServiceResult> Services;

        [OutputConstructor]
        private GetPublicCloudRegionResult(
            string continentCode,

            string datacenterLocation,

            string id,

            string name,

            string projectId,

            ImmutableArray<Outputs.GetPublicCloudRegionServiceResult> services)
        {
            ContinentCode = continentCode;
            DatacenterLocation = datacenterLocation;
            Id = id;
            Name = name;
            ProjectId = projectId;
            Services = services;
        }
    }
}
