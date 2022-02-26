// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package ovh

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Use this data source to retrieve information about an SSH key.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-ovh/sdk/go/ovh"
// 	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		_, err := ovh.LookupMeSSHKey(ctx, &GetMeSSHKeyArgs{
// 			KeyName: "mykey",
// 		}, nil)
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
func LookupMeSSHKey(ctx *pulumi.Context, args *LookupMeSSHKeyArgs, opts ...pulumi.InvokeOption) (*LookupMeSSHKeyResult, error) {
	var rv LookupMeSSHKeyResult
	err := ctx.Invoke("ovh:index/getMeSSHKey:getMeSSHKey", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getMeSSHKey.
type LookupMeSSHKeyArgs struct {
	// The name of the SSH key.
	KeyName string `pulumi:"keyName"`
}

// A collection of values returned by getMeSSHKey.
type LookupMeSSHKeyResult struct {
	// True when this public SSH key is used for rescue mode and reinstallations.
	Default bool `pulumi:"default"`
	// The provider-assigned unique ID for this managed resource.
	Id string `pulumi:"id"`
	// The content of the public key.
	// E.g.: "ssh-ed25519 AAAAC3..."
	Key string `pulumi:"key"`
	// See Argument Reference above.
	KeyName string `pulumi:"keyName"`
}

func LookupMeSSHKeyOutput(ctx *pulumi.Context, args LookupMeSSHKeyOutputArgs, opts ...pulumi.InvokeOption) LookupMeSSHKeyResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupMeSSHKeyResult, error) {
			args := v.(LookupMeSSHKeyArgs)
			r, err := LookupMeSSHKey(ctx, &args, opts...)
			return *r, err
		}).(LookupMeSSHKeyResultOutput)
}

// A collection of arguments for invoking getMeSSHKey.
type LookupMeSSHKeyOutputArgs struct {
	// The name of the SSH key.
	KeyName pulumi.StringInput `pulumi:"keyName"`
}

func (LookupMeSSHKeyOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupMeSSHKeyArgs)(nil)).Elem()
}

// A collection of values returned by getMeSSHKey.
type LookupMeSSHKeyResultOutput struct{ *pulumi.OutputState }

func (LookupMeSSHKeyResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupMeSSHKeyResult)(nil)).Elem()
}

func (o LookupMeSSHKeyResultOutput) ToLookupMeSSHKeyResultOutput() LookupMeSSHKeyResultOutput {
	return o
}

func (o LookupMeSSHKeyResultOutput) ToLookupMeSSHKeyResultOutputWithContext(ctx context.Context) LookupMeSSHKeyResultOutput {
	return o
}

// True when this public SSH key is used for rescue mode and reinstallations.
func (o LookupMeSSHKeyResultOutput) Default() pulumi.BoolOutput {
	return o.ApplyT(func(v LookupMeSSHKeyResult) bool { return v.Default }).(pulumi.BoolOutput)
}

// The provider-assigned unique ID for this managed resource.
func (o LookupMeSSHKeyResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v LookupMeSSHKeyResult) string { return v.Id }).(pulumi.StringOutput)
}

// The content of the public key.
// E.g.: "ssh-ed25519 AAAAC3..."
func (o LookupMeSSHKeyResultOutput) Key() pulumi.StringOutput {
	return o.ApplyT(func(v LookupMeSSHKeyResult) string { return v.Key }).(pulumi.StringOutput)
}

// See Argument Reference above.
func (o LookupMeSSHKeyResultOutput) KeyName() pulumi.StringOutput {
	return o.ApplyT(func(v LookupMeSSHKeyResult) string { return v.KeyName }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupMeSSHKeyResultOutput{})
}
