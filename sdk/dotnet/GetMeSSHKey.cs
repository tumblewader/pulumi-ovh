// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ovh
{
    public static class GetMeSSHKey
    {
        /// <summary>
        /// Use this data source to retrieve information about an SSH key.
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
        ///         var mykey = Output.Create(Ovh.GetMeSSHKey.InvokeAsync(new Ovh.GetMeSSHKeyArgs
        ///         {
        ///             KeyName = "mykey",
        ///         }));
        ///     }
        /// 
        /// }
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Task<GetMeSSHKeyResult> InvokeAsync(GetMeSSHKeyArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetMeSSHKeyResult>("ovh:index/getMeSSHKey:getMeSSHKey", args ?? new GetMeSSHKeyArgs(), options.WithDefaults());

        /// <summary>
        /// Use this data source to retrieve information about an SSH key.
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
        ///         var mykey = Output.Create(Ovh.GetMeSSHKey.InvokeAsync(new Ovh.GetMeSSHKeyArgs
        ///         {
        ///             KeyName = "mykey",
        ///         }));
        ///     }
        /// 
        /// }
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Output<GetMeSSHKeyResult> Invoke(GetMeSSHKeyInvokeArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetMeSSHKeyResult>("ovh:index/getMeSSHKey:getMeSSHKey", args ?? new GetMeSSHKeyInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetMeSSHKeyArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// The name of the SSH key.
        /// </summary>
        [Input("keyName", required: true)]
        public string KeyName { get; set; } = null!;

        public GetMeSSHKeyArgs()
        {
        }
    }

    public sealed class GetMeSSHKeyInvokeArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// The name of the SSH key.
        /// </summary>
        [Input("keyName", required: true)]
        public Input<string> KeyName { get; set; } = null!;

        public GetMeSSHKeyInvokeArgs()
        {
        }
    }


    [OutputType]
    public sealed class GetMeSSHKeyResult
    {
        /// <summary>
        /// True when this public SSH key is used for rescue mode and reinstallations.
        /// </summary>
        public readonly bool Default;
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        /// <summary>
        /// The content of the public key.
        /// E.g.: "ssh-ed25519 AAAAC3..."
        /// </summary>
        public readonly string Key;
        /// <summary>
        /// See Argument Reference above.
        /// </summary>
        public readonly string KeyName;

        [OutputConstructor]
        private GetMeSSHKeyResult(
            bool @default,

            string id,

            string key,

            string keyName)
        {
            Default = @default;
            Id = id;
            Key = key;
            KeyName = keyName;
        }
    }
}